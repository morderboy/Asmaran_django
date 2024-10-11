from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse, HttpResponseForbidden
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .models_master import Account, Vip
from .models_admin import AccountCharacter, CharacterMail
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.db import transaction
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.utils.timezone import now
#Redis
import redis
from django.conf import settings
from django.core.cache import cache

from .payment import pay_generation
import ipaddress
from ipware import get_client_ip

# Инициализация подключения к Redis
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

# Регистрация Пользователей
@csrf_exempt
@require_POST
@transaction.atomic
def register_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    user_email = data.get('email')

    if not User.objects.filter(username=username).exists():
        if not User.objects.filter(email=user_email).exists():
            user = User.objects.create_user(
                username=username,
                password=data.get('password'),
                email=user_email
            )

            account = Account.objects.using('master').create(
                username=username,
                password=user.password,  # Имейте в виду, что хранить пароли в открытом виде не рекомендуется
                email=user_email,
                status=1,  # Значение по умолчанию
                created_at=datetime.now(),
                last_modified_at=datetime.now(),
                coin_current=0,
                coin_total=0,
                current_world_id=1  # Установите нужный идентификатор мира
            )

            Vip.objects.using('master').create(
                account_id=account.id,
                character_oid=0,  # Если нужно, замените None на соответствующее значение
                world="1",  # Значение по умолчанию
                vip_level=0,
                vip_expire=0,
                vip_points=0
            )

            return login_view(request)
        else:
            return JsonResponse({
                'error': 'User already exists'
            }, status=401)

    else:
        return JsonResponse({
            'error': 'User already exists'
        }, status=400)

# Авторизация Пользователей
@csrf_exempt
@require_POST
def login_view(request):
    data = json.loads(request.body)
    identifier = data.get('username')  # Изменено на identifier
    password = data.get('password')

    try:
        # Проверяем, является ли идентификатор email или username
        if '@' in identifier:
            user = User.objects.get(email=identifier)
        else:
            user = User.objects.get(username=identifier)
    except User.DoesNotExist:
        user = None

    if user is not None:
        user = authenticate(username=user.username, password=password)
        if user is not None:
            login(request, user)
            csrf_token = get_token(request)
            response = JsonResponse({'success': True, 'username': user.username})
            response.set_cookie('csrftoken', csrf_token, httponly=False, secure=False, samesite='Strict')
            return response
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=403)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=403)


# Авторизация Пользователей лаунчера
@csrf_exempt
@require_POST
def login_app_view(request):
    data = json.loads(request.body)
    identifier = data.get('identifier')
    password = data.get('password')

    try:
        if '@' in identifier:
            user = User.objects.get(email=identifier)
        else:
            user = User.objects.get(username=identifier)
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=403)

    user = authenticate(username=user.username, password=password)
    if user is not None:
        # Проверяем, включена ли проверка бета-ключей
        site_settings = SiteSettings.objects.first()
        if site_settings.beta_key_check_enabled:
            try:
                beta_key = BetaKey.objects.get(user=user)
                if beta_key.is_expired():
                    return JsonResponse({'success': False, 'error': 'Действие ключа ЗБТ истекло'}, status=403)
            except BetaKey.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Необходим ключ ЗБТ'}, status=403)

        # Логиним пользователя
        login(request, user)
        response = JsonResponse({'success': True})
        return response
    else:
        return JsonResponse({'success': False, 'error': 'Неверные данные'}, status=403)


@csrf_exempt
@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'User logged out successfully'})


@csrf_exempt
@require_POST
def password_recovery_view(request):
    data = json.loads(request.body)
    email = data.get('email')

    try:
        user = User.objects.get(email=email)
        reset_token = PasswordResetToken.create_token(user)
        # Генерация ссылки для восстановления пароля (например, с использованием токена)
        recovery_link = f"http://pybyte.ru/password-reset/{reset_token.token}/"  # Пример ссылки

        # Отправка письма на email пользователя
        send_mail(
            'Восстановление пароля',
            f'Для восстановления пароля перейдите по следующей ссылке: {recovery_link}',
            'asmorantest@pybyte.ru',
            [email],
            fail_silently=False,
        )

        return JsonResponse({'success': True, 'message': 'Письмо для восстановления пароля отправлено.'})
    except User.DoesNotExist:
        return JsonResponse({'success': True, 'message': 'Письмо для восстановления пароля отправлено.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    
@require_POST
def password_recovery_direct_view(request):
    try:
        # Получаем CSRF токен из запроса (он автоматически проверяется, если нет декоратора csrf_exempt)
        csrf_token = request.META.get('CSRF_COOKIE')

        if not csrf_token:
            return JsonResponse({'error': 'CSRF token missing'}, status=400)

        # Ищем пользователя по CSRF токену (этот шаг требует, чтобы у вас была связь между пользователем и его CSRF токеном)
        user = request.user

        if not user:
            return JsonResponse({'error': 'User not found'}, status=404)

        # Создаем токен для сброса пароля
        reset_token = PasswordResetToken.create_token(user)

        # Возвращаем токен для сброса пароля
        return JsonResponse({'success': True, 'reset_token': reset_token.token})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_POST
def password_recovery_confirm_view(request):
    token = request.GET.get('token')

    try:
        reset_token = PasswordResetToken.objects.get(token=token)
    except PasswordResetToken.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=400)

    if reset_token.is_expired():
        return JsonResponse({'error': 'Token has expired'}, status=401)

    # Если токен валиден и не истек, возвращаем id пользователя
    return JsonResponse({'success': 'Token is valid'})


@csrf_exempt
@require_POST
def password_reset_view(request):
    data = json.loads(request.body)
    token = data.get('token')
    new_password = data.get('password')

    try:
        reset_token = PasswordResetToken.objects.get(token=token)
    except PasswordResetToken.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=400)

    if reset_token.is_expired():
        return JsonResponse({'error': 'Token has expired'}, status=401)

    # Если токен валиден и не истек, меняем пароль пользователя
    user = reset_token.user
    user.set_password(new_password)
    user.save()

    # Переаутентификация пользователя, если он уже аутентифицирован
    if request.user.is_authenticated:
        login(request, user)
    else:
        # Если пользователь не аутентифицирован, аутентифицируем его для сессии
        user = authenticate(username=user.username, password=new_password)
        if user is not None:
            login(request, user)

    # Удаляем использованный токен
    reset_token.delete()

    return JsonResponse({'success': 'Password has been reset successfully'})


@csrf_exempt
@api_view(['GET'])
def product_list_view(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 6))
    offset = (page - 1) * page_size
    products = Product.objects.all()[offset:offset + page_size]
    serializer = ShortProductSerializer(products, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def news_list_view(request):
    state = int(request.GET.get('state', 0))
    news = News.objects.all().order_by('-date')

    if state == 0:
        news = news[3:]  # Slice the queryset here
    else:
        news = news[:3]  # Slice the queryset here

    serializer = ShortNewsSerializer(news, many=True)  # Pass the sliced queryset to the serializer
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def news_list_app_view(request):
    news = News.objects.all().order_by('-date')

    news = news[:2]  # Slice the queryset here
    serializer = ShortNewsSerializer(news, many=True)  # Pass the sliced queryset to the serializer
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def new_news_list_app_view(request):
    try:
        # Получаем список существующих ID из тела запроса
        existing_ids = json.loads(request.body)

        print(f"Received existing IDs: {existing_ids}")

        # Получаем новости, которых нет в списке существующих ID, сортируем по дате
        latest_news = News.objects.all().order_by('-date')[:2]

        latest_news_ids = [news.id for news in latest_news]
        print(f"Received latest_news_ids: {latest_news_ids}")

        if set(latest_news_ids) != set(existing_ids):
            # Если ID не совпадают, возвращаем последние две новости
            serializer = ShortNewsSerializer(latest_news, many=True)
            return Response(serializer.data)
        else:
            # Если совпадают, возвращаем пустой список
            return Response([])

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@api_view(['GET'])
def news_detail_view(request, news_id):
    try:
        news = News.objects.get(id=news_id)
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def check_moderator_or_staff(request):
    user = request.user
    if user.is_authenticated:
        cache_key = f"user_is_staff_{user.username}"
        cache_key_two = f"user_is_moderator_{user.username}"
        is_staff = cache.get(cache_key)
        is_moderator = cache.get(cache_key_two)

        if is_staff is None or is_moderator is None:
            is_moderator = user.groups.filter(name='moderators').exists()
            is_staff = user.is_staff
            cache.set(cache_key, is_staff, timeout=60*60)
            cache.set(cache_key_two, is_moderator, timeout=60*60)
        if is_moderator or is_staff:
            return JsonResponse({'result': True})
        else:
            return JsonResponse({'result': False})
    else:
        return JsonResponse({'result': False}, status=401)

@api_view(['GET'])
def get_balance(request):
    user = request.user
    if user.is_authenticated:
        cache_key = f"user_balance_{user.username}"  # Уникальный ключ для каждого пользователя
        balance = cache.get(cache_key)

        if balance is None:
            try:
                account = Account.objects.using('master').get(username=user.username)
                balance = account.coin_current

                # Сохранение баланса в Redis на 60 секунд
                cache.set(cache_key, balance, timeout=600)
            except Account.DoesNotExist:
                return JsonResponse({'result': False, 'error': 'Account not found'}, status=404)

        return JsonResponse({'result': True, 'balance': balance})
    else:
        return JsonResponse({'result': False}, status=401)

@require_POST
def buy_coins(request):
    user = request.user
    if user.is_authenticated:
        try:
            account = Account.objects.using('master').get(username=user.username)
            data = json.loads(request.body)
            coins_to_add = int(data.get('rubls'))  # Получаем количество коинов из POST-запроса

            if (coins_to_add <= 0):
                raise ValueError

            count = Orders.objects.count()
            p_url, p_id, p_created_at = pay_generation(coins_to_add, count + 1, user.email)

            if p_url and p_id and p_created_at:
                order = Orders.objects.create(
                    id = p_id,
                    user = user,
                    created_at = p_created_at,
                    coins = coins_to_add
                )

                if order:
                    return JsonResponse({'result': True, 'payment_url': p_url})

            return JsonResponse({'result': False, 'error': "Cant generate payment url"}, status=402)

        except Account.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Account not found'}, status=404)
        except ValueError:
            return JsonResponse({'result': False, 'error': 'Invalid rubls value'}, status=400)
    else:
        return JsonResponse({'result': False}, status=401)

@require_GET
def get_characters_list(request):
    user = request.user
    if user.is_authenticated:
        try:
            account = Account.objects.using('master').get(username=user.username)
            characters = AccountCharacter.objects.using('admin').filter(accountid=account.id)
            if not characters.exists():
                return JsonResponse({'result': False, 'error': 'No characters found for this account'}, status=405)
            serializer = AccountCharacterSerializer(characters, many=True)
            return JsonResponse({'result': True, 'characters': serializer.data}, status=200)
        except Account.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Account not found'}, status=404)
    else:
        return JsonResponse({'result': False}, status=401)

@require_POST
def buy_product(request):
    user = request.user
    if user.is_authenticated:
        try:
            data = json.loads(request.body)
            character_id = int(data.get('character_id'))
            product_id = int(data.get('product_id'))

            # Получаем учетную запись пользователя
            account = Account.objects.using('master').get(username=user.username)

            # Получаем персонажа, связанного с этой учетной записью и указанным character_id
            character = AccountCharacter.objects.using('admin').get(accountid=account.id, characterid=character_id)

            # Получаем продукт по product_id
            product = Product.objects.get(id=product_id)

            # Получаем связанный с продуктом шаблон предмета
            item_template = product.get_item_template()

            # Выполняем логику покупки (это может включать списание коинов, добавление предмета персонажу и т.д.)
            if account.coin_current >= product.price:
                account.coin_current -= product.price
                account.save(using='master')

                # Сохраняем баланс в редис
                cache_key = f"user_balance_{user.username}"
                cache.set(cache_key, account.coin_current, timeout=600)

                # Отправляем предмет на почту в игре
                CharacterMail.objects.using('admin').create(
                    mailarchive=0,
                    isaccountmail=0,
                    recipientid=character.characterid,  # ID аккаунта
                    recipientname=character.charactername,  # Имя аккаунта
                    senderid=1,  # ID отправителя (1 для Admin)
                    sendername='Admin',  # Имя отправителя
                    mailread=0,  # Письмо не прочитано
                    mailsubject='Покупка в магазине Asmaran',  # Тема письма
                    mailmessage='',  # Сообщение
                    cod=0,
                    mailattachmentitemid1=item_template.id,  # ID предмета в письме (из шаблона)
                    mailattachmentitemid1taken=0,  # Предмет не забран
                    datecreated=now(),  # Дата создания письма
                    dateupdated=now(),  # Дата обновления
                    expiry=None  # Время истечения (оставляем null)
                )

                # Возвращаем успешный ответ с данными персонажа и купленного товара
                character_serializer = AccountCharacterSerializer(character)
                return JsonResponse({
                    'result': True,
                    'character': character_serializer.data,
                    'product': product.title
                }, status=200)
            else:
                return JsonResponse({'result': False, 'error': 'Insufficient balance'}, status=400)

        except Account.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Account not found'}, status=402)
        except AccountCharacter.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Character not found'}, status=403)
        except Product.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'result': False, 'error': 'Unauthorized'}, status=401)

@require_POST
def buy_zbt_key(request):
    site_settings = SiteSettings.objects.first()
    if not site_settings.beta_key_check_enabled:
        return JsonResponse({'result': False, 'error': 'API Forbidden'}, status=403)

    user = request.user
    if user.is_authenticated:
        try:
            data = json.loads(request.body)
            product_id = int(data.get('product_id'))

            # Получаем учетную запись пользователя
            account = Account.objects.using('master').get(username=user.username)

            # Получаем продукт по product_id
            product = Product.objects.get(id=product_id)

            # Выполняем логику покупки (это может включать списание коинов, добавление предмета персонажу и т.д.)
            if account.coin_current >= product.price:
                account.coin_current -= product.price
                account.save(using='master')

                # Сохраняем баланс в редис
                cache_key = f"user_balance_{user.username}"
                cache.set(cache_key, account.coin_current, timeout=600)
                    
                # Проверяем, есть ли уже ключ ЗБТ у пользователя
                try:
                    beta_key = BetaKey.objects.get(user=user)
                    # Если ключ найден, продлеваем его на 30 дней
                    if beta_key.expiration_date < now():
                        beta_key.expiration_date = now() + timedelta(days=30)
                    else:
                        # Если ключ еще действителен, продлеваем на 30 дней от текущей даты окончания
                        beta_key.expiration_date += timedelta(days=30)
                    beta_key.save()
                    message = 'Ваш ключ ЗБТ продлен на 30 дней.'
                except BetaKey.DoesNotExist:
                    # Если ключа нет, создаем новый с действием на 30 дней
                    expiration_date = now() + timedelta(days=30)
                    key = str(uuid.uuid4())  # Генерация уникального ключа
                    BetaKey.objects.create(user=user, key=key, expiration_date=expiration_date)
                    message = 'Вы успешно приобрели ключ ЗБТ.'

                return JsonResponse({
                    'result': True,
                    'product': product.title
                }, status=200)
            else:
                return JsonResponse({'result': False, 'error': 'Insufficient balance'}, status=400)

        except Account.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Account not found'}, status=402)
        except Product.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'result': False, 'error': 'Unauthorized'}, status=401)

@require_POST
@csrf_exempt
def payment_notification(request):
    # Список разрешённых IP-диапазонов и IP-адресов
    ALLOWED_NETWORKS = [
        ipaddress.ip_network('185.71.76.0/27'),
        ipaddress.ip_network('185.71.77.0/27'),
        ipaddress.ip_network('77.75.153.0/25'),
        ipaddress.ip_network('77.75.154.128/25'),
        ipaddress.ip_network('2a02:5180::/32'),
    ]

    # Список разрешённых конкретных IP-адресов
    ALLOWED_IPS = [
        ipaddress.ip_address('77.75.156.11'),
        ipaddress.ip_address('77.75.156.35'),
    ]

    ip, is_routable = get_client_ip(request, request_header_order=['HTTP_X_FORWARDED_FOR', 'HTTP_X_REAL_IP'])

    # Преобразуем IP в объект
    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        return HttpResponseForbidden('Invalid IP')

    # Проверяем, находится ли IP в разрешённых сетях или это конкретный разрешённый IP
    if not (any(ip_obj in net for net in ALLOWED_NETWORKS) or ip_obj in ALLOWED_IPS):
        return HttpResponseForbidden('Access denied')

    data = json.loads(request.body)
    id = data.get("object").get("id")
    if not id:
        return JsonResponse({'result': False}, status=400)

    try:
        # Сохраняем статус заказа как подтверждённый
        order = Orders.objects.get(id=id)

        # Если заказ уже был выдан, пропускаем
        if order.status == 'issued':
            return JsonResponse({'result': True}, status=200)
        
        order.status = "confirmed"
        order.save()

        # Обрабатываем заказ
        username = order.user.username
        account = Account.objects.using('master').get(username=username)
        account.coin_current += order.coins
        account.coin_total += order.coins
        account.save(using='master')

        vip = Vip.objects.using('master').get(account_id=account.id)
        vip.vip_points += order.coins

        # Переводим заказ в статус выдан
        order.status = "issued"
        order.save()

        # Обновляем данные о коинах в Redis
        cache_key = f"user_balance_{username}"
        cache.set(cache_key, account.coin_current, timeout=600)
        
        return JsonResponse({'result': True}, status=200)
        
    except Orders.DoesNotExist:
        return JsonResponse({'result': False}, status=400)
    except Account.DoesNotExist:
        return JsonResponse({'result': False}, status=400)
    except Vip.DoesNotExist:
        return JsonResponse({'result': False}, status=400)
    except Exception as e:
        return JsonResponse({'result': False}, status=400)