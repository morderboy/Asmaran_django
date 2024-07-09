from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json

# Регистрация Пользователей
@csrf_exempt
@require_POST
def register_view(request):
    data = json.loads(request.body)
    username = data.get('username')

    if not User.objects.filter(username=username).exists():
        User.objects.create_user(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email')
        )

        return login_view(request)

    else:
        return JsonResponse({
            'error': 'User already exists'
        }, status=400)

# Авторизация Пользователей
@csrf_exempt
@require_POST
def login_view(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None

    if user is not None:
        user = authenticate(username=user.username, password=password)
        if user is not None:
            login(request, user)
            csrf_token = get_token(request)
            response = JsonResponse({'success': True, 'id': user.id})
            response.set_cookie('csrftoken', csrf_token, httponly=True, secure=True, samesite='Strict')
            return response
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=403)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=403)
