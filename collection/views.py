from django.shortcuts import render
from products.models import *
# Create your views here.


def collection(request):
	products = ProductImage.objects.filter(is_active=True)
	products_fridge = products.filter(product__product_variant__id = 1).order_by('-created')[:3]
	products_microwave = products.filter(product__product_variant__id = 2).order_by('-created')[:3]
	products_coffee = products.filter(product__product_variant__id = 3).order_by('-created')[:3]
	products_multiwriters = products.filter(product__product_variant__id = 4).order_by('-created')[:3]

	return render(request, 'collection/collection_page.html', locals())

def fridge(request):
	products = ProductImage.objects.filter(is_active=True)
	products_fridge = products.filter(product__product_variant__id = 1).order_by('-created')[:12]

	return render(request, 'collection/fridge_page.html', locals())

def microwave(request):
	products = ProductImage.objects.filter(is_active=True)
	products_microwave = products.filter(product__product_variant__id = 2).order_by('-created')[:12]

	return render(request, 'collection/microwave_page.html', locals())

def coffee(request):
	products = ProductImage.objects.filter(is_active=True)
	products_coffee = products.filter(product__product_variant__id = 3).order_by('-created')[:12]

	return render(request, 'collection/coffee_page.html', locals())

def multiwriters(request):
	products = ProductImage.objects.filter(is_active=True)
	products_multiwriters = products.filter(product__product_variant__id = 4).order_by('-created')[:12]

	return render(request, 'collection/multiwriters_page.html', locals())