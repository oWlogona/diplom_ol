from .models import *

def getting_basket_info(request):
	session_key = request.session.session_key
	if not session_key:
		request.session['session_key'] = 123
		request.session.cycle_key()

	products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True).exclude(order__isnull=False)
	products_total_amount = products_in_basket.count()
	return locals()