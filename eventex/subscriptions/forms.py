
from django import forms
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf
from django.core.exceptions import ValidationError


class SubscriptionForm(forms.Form):
	name = forms.CharField(label="Nome")
	cpf = forms.CharField(label="CPF", validators=[validate_cpf])
	email = forms.EmailField(label="E-mail", required=False)
	phone = forms.CharField(label="Telefone", required=False)

	def clean_name(self):
		name = self.cleaned_data['name']
		words = [w.capitalize() for w in name.split()]
		return ' '.join(words)

	def clean(self):
		if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
		   raise ValidationError('Informe seu e-mail ou telefone.')

		return self.cleaned_data
	
"""
class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = ['name', 'cpf', 'email', 'phone']

	def clean_name(self):
		name = self.cleaned_data['name']
		words = [w.capitalize() for w in name.split()]
		return ' '.join(words)

	def clean_name(self):
		name = self.cleaned_data['name']
		words = [w.capitalize() for w in name.split()]
		return ' '.join(words)"""