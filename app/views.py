from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product, News, PasswordResetToken, BetaKey, SiteSettings
from .models_master import Account, Vip
from .serializers import ProductSerializer, ShortProductSerializer, NewsSerializer, ShortNewsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.db import transaction
from datetime import datetime
from django.core.mail import send_mail


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
    identifier = data.get('identifier')  # Изменено на identifier
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
        is_moderator = user.groups.filter(name='moderators').exists()
        is_staff = user.is_staff
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
        try:
            account = Account.objects.using('master').get(username=user.username)
            return JsonResponse({'result': True, 'balance': account.coin_current})
        except Account.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Account not found'}, status=404)
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

            if (coins_to_add == 0):
                raise ValueError

            # Добавляем коины к текущему балансу
            account.coin_current += coins_to_add
            print(coins_to_add)
            account.coin_total += coins_to_add
            account.save(using='master')  # Сохраняем изменения в базе данных

            return JsonResponse({'result': True, 'balance': account.coin_current})
        except Account.DoesNotExist:
            return JsonResponse({'result': False, 'error': 'Account not found'}, status=404)
        except ValueError:
            return JsonResponse({'result': False, 'error': 'Invalid rubls value'}, status=400)
    else:
        return JsonResponse({'result': False}, status=401)