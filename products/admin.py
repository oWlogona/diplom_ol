from django.contrib import admin
from .models import *

# Register your models here.

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]
	inlines = [ProductImageInline]

class ProductImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields]

class Product_variantAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product_variant._meta.fields]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product_variant, Product_variantAdmin)