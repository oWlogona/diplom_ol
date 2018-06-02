from django import forms
from .models import Asking

class AskingForm(forms.ModelForm):

	class Meta:
		model = Asking
		fields = ['name', 'email', 'text_asking']