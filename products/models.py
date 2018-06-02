from django.db import models

# Create your models here.

class Product_variant(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тип продукту'
		verbose_name_plural = 'Тип продукту'

class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	product_variant = models.ForeignKey(Product_variant, blank=True, null=True, default=None, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товари'

class ProductImage(models.Model):
	product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='static/media/media_product/')
	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Світлина'
		verbose_name_plural = 'Світлини'