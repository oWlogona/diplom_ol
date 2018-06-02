from django.contrib import admin
from .models import *

# Register your models here.

class SubscribeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Subscribe._meta.fields]

admin.site.register(Subscribe, SubscribeAdmin)