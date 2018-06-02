from django.db import models

# Create your models here.

class Status(models.Model):
	type_answer = models.CharField(max_length=25)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.type_answer

class TypeQuestion(models.Model):
	type_question = models.CharField(max_length=25)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.type_question

class Asking(models.Model):
	status = models.ForeignKey(Status, blank=True, null=True, default=None, on_delete=models.CASCADE)
	type_question = models.ForeignKey(TypeQuestion, blank=True, null=True, default=None, on_delete=models.CASCADE)
	name = models.CharField(max_length=56)
	email = models.EmailField()
	text_asking = models.TextField()
	text_answer = models.TextField(blank=True, null=True,)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name
