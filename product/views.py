from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import CategoryForm, ProductForm
# Create your views here.
def index(request):
    products = Product.objects.filter(available=True)
    contxt = {
        'products':products
    }
    return render(request, 'index.html', contxt)


def product_detail(request, slug=None):
    product = Product.objects.get(slug=slug)
    contxt = {
        'product':product
    }
    return render(request, 'product_detail.html', contxt)


def product_admin(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    form_category = CategoryForm()
    form_product = ProductForm()
    contxt = {
        'categorys':categorys,
        'products':products,
        'form_category':form_category,
        'form_product':form_product
    }
    return render(request, 'admin/product.html', contxt)

def add_categorys(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('product_admin')


def update_categorys(request, id=None):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('product_admin')
    contxt = {
        'form':form
    }
    return render(request, 'admin/forms.html', contxt)

def delete_categorys(request, id=None):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('product_admin')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('product_admin')


def update_product(request, id=None):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_admin')
    contxt = {
        'form':form
    }
    return render(request, 'admin/forms.html', contxt)


def delete_product(request, id=None):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_admin')


# API
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def categoryCreate(request):
	serializer = CategorySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['GET'])
def categoryList(request):
	Products = Category.objects.all().order_by('-id')
	serializer = CategorySerializer(Products, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
	serializer = ProductSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['GET'])
def productList(request):
	Products = Product.objects.all().order_by('-id')
	serializer = ProductSerializer(Products, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
	Products = Product.objects.get(id=pk)
	serializer = ProductSerializer(Products, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def productUpdate(request, pk):
	Products = Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=Products, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
	Products = Product.objects.get(id=pk)
	Products.delete()
	return Response('delete ok')
