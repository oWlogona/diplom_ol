from django.shortcuts import render
from .forms import *
from products.models import *
# Create your views here.

def landing(request):
	products = ProductImage.objects.filter(is_active = True, is_main = True, product__is_active=True)
	products_ordered = products.order_by('-created')[:3]
	products_fridge = products.filter(product__product_variant__id = 1).order_by('-created')[:3]
	products_microwave = products.filter(product__product_variant__id = 2).order_by('-created')[:3]
	products_coffee = products.filter(product__product_variant__id = 3).order_by('-created')[:3]
	products_multiwriters = products.filter(product__product_variant__id = 4).order_by('-created')[:3]

	if request.method == 'POST':
		email = request.POST.get('email')
		name = email.split('@')[0]
		Subscribe.objects.create(email=email, name=name)

	return render(request, 'landing/landing_content.html', locals())
