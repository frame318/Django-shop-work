from django.contrib import admin
from .models import Category, Product
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AdminProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
