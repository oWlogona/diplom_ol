from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def contact(request):
	form = AskingForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
	return render(request, 'contact/contact.html', locals())

def faq(request):
	form_ship = Asking.objects.filter(type_question__type_question='Технические', status__type_answer='Решен')
	form_return = Asking.objects.filter(type_question__type_question='Покупки', status__type_answer='Решен')
	print(Asking.objects.filter())
	return render(request, 'faq/faq.html', locals())
