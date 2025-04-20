from django import forms
from django.core.exceptions import ValidationError

from constants import BANNED_WORDS
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name').lower()
        description = cleaned_data.get('description').lower()

        for word in BANNED_WORDS:
            if word.lower() in name or word.lower() in description:
                raise ValidationError(f'Поле содержит запрещенное слово - "{word}", просьба исправить на другое')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in BANNED_WORDS:
            if word.lower() in name:
                raise ValidationError(f'Поле содержит запрещенное слово - "{word}", просьба исправить на другое')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in BANNED_WORDS:
            if word.lower() in description:
                raise ValidationError(f'Поле содержит запрещенное слово - "{word}", просьба исправить на другое')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    # def clean_image(self):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('@example.com'):
    #         raise ValidationError('Email должен оканчиваться на @example.com')
    #     return email
