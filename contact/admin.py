from django.contrib import admin
from .models import *
# Register your models here.

class AskingClass(admin.ModelAdmin):
	list_display = [field.name for field in Asking._meta.fields]

class StatusClass(admin.ModelAdmin):
	list_display = [field.name for field in Status._meta.fields]

class TypeQuestionClass(admin.ModelAdmin):
	list_display = [field.name for field in TypeQuestion._meta.fields]


admin.site.register(Asking, AskingClass)
admin.site.register(Status, StatusClass)
admin.site.register(TypeQuestion, TypeQuestionClass)