from django.urls import path
from . import views

urlpatterns = [
	path('bassker_adding/', views.bassker_adding, name="bassker_adding"),
	path('checkout/', views.checkout, name='checkout'),
]