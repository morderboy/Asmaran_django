"""
URL configuration for Asmaran_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/select2/', include('django_select2.urls')),
    path('api/user/register', views.register_view),
    path('api/user/login', views.login_view),
    path('api/user/applogin', views.login_app_view),
    path('api/logout', views.logout_view),
    path('api/password-recovery', views.password_recovery_view),
    path('api/password-recovery-direct', views.password_recovery_direct_view),
    path('api/password-recovery-confirm', views.password_recovery_confirm_view),
    path('api/password-reset/', views.password_reset_view),
    path('api/shop/', views.product_list_view),
    path('api/shop/product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('api/news/', views.news_list_view),
    path('api/app/news/', views.news_list_app_view),
    path('api/app/newnews', views.new_news_list_app_view),
    path('api/news/<int:news_id>/', views.news_detail_view, name='news_detail'),
    path('api/check-moderator-or-staff/', views.check_moderator_or_staff),
    path('api/balance', views.get_balance),
    path('api/buy-coins', views.buy_coins),
    path('api/characters-list', views.get_characters_list)
]
