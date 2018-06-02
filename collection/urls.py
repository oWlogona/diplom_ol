from django.urls import path
from . import views

urlpatterns = [
	path('multiwriters', views.multiwriters, name="multiwriters"),
	path('collection', views.collection, name="collection"),
	path('microwave', views.microwave, name="microwave"),
	path('fridge', views.fridge, name="fridge"),
	path('coffee', views.coffee, name="coffee"),
]