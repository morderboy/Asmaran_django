from rest_framework import serializers
from .models import Product, News
from .models_admin import AccountCharacter


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image_url']


class ShortProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image_url']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image_url', 'date', 'title', 'description']


class ShortNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image_url', 'date', 'title']

class AccountCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCharacter
        fields = ['characterid', 'charactername']

