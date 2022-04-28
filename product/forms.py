from django.forms import ModelForm
from .models import Category, Product
from django import forms


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'description', 'category', 'price', 'stock', 'available']
