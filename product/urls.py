from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/detail/<slug:slug>', views.product_detail, name='product_detail'),

    path('admin-product/', views.product_admin, name='product_admin'),

    path('add-categorys/', views.add_categorys, name='add_categorys'),
    path('update-categorys/<int:id>', views.update_categorys, name='update_categorys'),
    path('delete-categorys/<int:id>', views.delete_categorys, name='delete_categorys'),


    path('add-products/', views.add_product, name='add_product'),
    path('update-product/<int:id>', views.update_product, name='update_product'),
    path('delete-product/<int:id>', views.delete_product, name='delete_product'),

    #API

    path('category-create/', views.categoryCreate, name="categoryCreate"),
    path('category-list/', views.categoryList, name="categoryList"),

    path('product-create/', views.productCreate, name="productCreate"),
    path('product-list/', views.productList, name="productList"),
    path('product-detailt/<int:pk>/', views.productDetail, name="productDetail"),
    path('product-update/<int:pk>/', views.productUpdate, name="productUpdate"),
    path('product-delete/<int:pk>/', views.productDelete, name="productDelete"),
]
