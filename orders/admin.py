from django.contrib import admin
from .models import *

# Register your models here.

class ProductInOrderInline(admin.TabularInline):
	model = ProductInOrder
	extra = 1

class OrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	inlines = [ProductInOrderInline]

class StatusAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Status._meta.fields]

class ProductInOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductInOrder._meta.fields]

class ProductInBasketAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductInBasket._meta.fields]

	class Meta:
		model = ProductInBasket


admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(ProductInBasket, ProductInBasketAdmin)