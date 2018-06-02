from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User

# Create your views here.

def bassker_adding(request):
	return_dict = dict()
	session_key = request.session.session_key
	print(request.POST)
	data = request.POST
	product_id = data.get("product_id")
	number = data.get("amount")
	is_delete = data.get("is_delete")

	if is_delete == 'true':
		ProductInBasket.objects.filter(id=product_id).update(is_active=False)
	else:
		new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, 
			product_id=product_id, is_active=True, defaults={"number": number})
		
		if not created:
			new_product.number += int(number)
			new_product.save(force_update=True)
			
	products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
	products_total_number = products_in_basket.count()
	return_dict['products_total_number'] = products_total_number

	return_dict['products'] = list()

	for item in products_in_basket:
		product_dict = dict()
		product_dict['id'] = item.id
		product_dict['name'] = item.product.name
		product_dict['price_per_item'] = item.price_per_item
		product_dict['number'] = item.number 
		return_dict['products'].append(product_dict)

	return JsonResponse(return_dict)


def checkout(request):
	session_key = request.session.session_key
	products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True).exclude(order__isnull=False)

	form = CheckoutContactForm(request.POST or None)
	if request.POST:
		if form.is_valid():
			data = request.POST
			phone = data.get('phone')
			name = data.get('name')
			user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})

			order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

			for item, values in data.items():
				if item.startswith("product_in_basket_"):
					product_in_basket_id = item.split('product_in_basket_')[1]
					product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
					product_in_basket.number = values
					product_in_basket.order = order
					product_in_basket.is_active = False
					product_in_basket.save(force_update=True)

					ProductInOrder.objects.create(product=product_in_basket.product, number=product_in_basket.number,
						price_per_item=product_in_basket.price_per_item, total_price=product_in_basket.total_price,
						order=order)
		else:
			print('NIXT')
	return render(request, 'check_out/checkout.html', locals())