from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models_world_content import ItemTemplates
import uuid


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.ImageField(upload_to="images/prod")
    item_template_id = models.IntegerField(null=True, blank=True)

    def get_item_template(self):
        return ItemTemplates.objects.using('world_content').get(id=self.item_template_id)

    def __str__(self):
        return self.title


class News(models.Model):
    image_url = models.ImageField(upload_to="images/news")
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class BetaKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f'{self.key} for {self.user.username}'

    def is_expired(self):
        return timezone.now() > self.expiration_date


class SiteSettings(models.Model):
    beta_key_check_enabled = models.BooleanField(default=True)

    def __str__(self):
        return "Site Settings"


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    token = models.CharField(max_length=64)  # Токен в открытом виде
    expires_at = models.DateTimeField()  # Дата истечения токена

    def __str__(self):
        return f"Password reset token for {self.user.username}"

    def is_expired(self):
        """Проверяет, истек ли токен."""
        return timezone.now() > self.expires_at

    @classmethod
    def create_token(cls, user):
        """Создает новый токен для пользователя."""
        token = uuid.uuid4().hex  # Генерация уникального токена
        expires_at = timezone.now() + timedelta(hours=1)  # Токен действует 1 час
        return cls.objects.create(user=user, token=token, expires_at=expires_at)
