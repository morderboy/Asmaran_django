from django import forms
from django_select2.forms import ModelSelect2Widget
from .models_world_content import ItemTemplates
from .widgets import CustomModelSelect2Widget
from .models import Product
from django.contrib.auth.models import User

class ProductAdminForm(forms.ModelForm):
    item_template = forms.ModelChoiceField(
        queryset=ItemTemplates.objects.using('world_content').only('id', 'name'),
        required=False,
        label="Item Template",
        widget=CustomModelSelect2Widget(
            model=ItemTemplates,
            search_fields=['id__icontains', 'name__icontains'],  # Фильтрация по ID и имени
            attrs={'data-placeholder': 'Select an item', 'style': 'width: 100%;'}
        )
    )

    class Meta:
        model = Product
        exclude = ('item_template_id', "title")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.item_template_id:
            self.fields['item_template'].initial = ItemTemplates.objects.using('world_content').get(id=self.instance.item_template_id)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['item_template']:
            instance.item_template_id = self.cleaned_data['item_template'].id
            instance.title = self.cleaned_data['item_template'].name
        if commit:
            instance.save()
        return instance


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])  # Хешируем пароль
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user