from django import forms
from django.forms import BooleanField

from .models import Product, Version, Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ["name", "price", "category", "preview", "description", 'manufactured_at', ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(word in name.lower() for word in self.FORBIDDEN_WORDS):
            raise forms.ValidationError("Название продукта содержит запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in self.FORBIDDEN_WORDS):
            raise forms.ValidationError("Описание продукта содержит запрещенные слова.")
        return description

class ProductModeratorForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ["sing_of_publication", "description", "category"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(word in name.lower() for word in self.FORBIDDEN_WORDS):
            raise forms.ValidationError("Название продукта содержит запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in self.FORBIDDEN_WORDS):
            raise forms.ValidationError("Описание продукта содержит запрещенные слова.")
        return description


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading', 'content', 'slug', 'preview', 'sing_of_publication']


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
        widgets = {
            'version_number': forms.TextInput(attrs={'class': 'form-control'}),
            'version_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
