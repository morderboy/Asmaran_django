from django.contrib import admin
from .models import News, BetaKey, SiteSettings
from .models_master import Account, Vip
from django.utils import timezone
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
import uuid
from datetime import timedelta
from .forms import ProductAdminForm, Product, User, UserCreationForm, UserChangeForm
from datetime import datetime

# Register your models here.

admin.site.register(News)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title', 'description', 'price', 'image_url', 'item_template_id')
    search_fields = ('title',)
    list_filter = ('price',)
    fields = ['item_template', 'description', 'price', 'image_url']

    def item_template(self, obj):
        if obj.item_template_id:
            return obj.get_item_template().name
        return None
    item_template.short_description = 'Item Template'


@admin.register(BetaKey)
class BetaKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'expiration_date', 'is_expired')
    search_fields = ('user__username', 'key')
    list_filter = ('expiration_date',)


def add_beta_key_to_user(modeladmin, request, queryset):
    expiration_date = timezone.now() + timedelta(days=30)  # Устанавливаем срок действия на 30 дней
    for user in queryset:
        key = str(uuid.uuid4())  # Генерация уникального ключа
        BetaKey.objects.create(user=user, key=key, expiration_date=expiration_date)
    modeladmin.message_user(request, "Бета-ключи успешно добавлены выбранным пользователям.")


add_beta_key_to_user.short_description = "Добавить бета-ключ выбранным пользователям"


# Получаем текущий зарегистрированный UserAdmin
class UserAdmin(BaseUserAdmin):
    actions = [add_beta_key_to_user]

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

    def save_model(self, request, obj, form, change):
        # Сначала сохраняем пользователя, чтобы он был создан в базе данных
        super().save_model(request, obj, form, change)

        # Создаем запись в таблице Account в базе данных master
        account = Account.objects.using('master').create(
            username=obj.username,
            password=obj.password,  # Имейте в виду, что хранить пароли в открытом виде не рекомендуется
            email=obj.email,
            status=1,  # Значение по умолчанию
            created_at=datetime.now(),
            last_modified_at=datetime.now(),
            coin_current=0,
            coin_total=0,
            current_world_id=1  # Установите нужный идентификатор мира
        )

        # Создаем запись в таблице Vip в базе данных master
        Vip.objects.using('master').create(
            account_id=account.id,
            character_oid=0,  # Если нужно, замените None на соответствующее значение
            world="1",  # Значение по умолчанию
            vip_level=0,
            vip_expire=0,
            vip_points=0
        )


# Перерегистрируем UserAdmin с добавленным действием
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('beta_key_check_enabled',)