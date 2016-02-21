
from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r 

from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

	def setUp(self):
		self.obj = Subscription(
				name='Henrique Bastos',
				cpf='12345678901',
				email='henrique@bastos.net',
				phone='21-996186180',
			)
		self.obj.save()

	def test_create(self):
		self.assertTrue(Subscription.objects.exists())

	def test_created_at(self):
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_str(self):
		self.assertEqual('Henrique Bastos', str(self.obj))

	def test_paid_default_to_false(self):
		""" By default paid must be False. """
		self.assertEqual(False, self.obj.paid)


class TemplateRegressionTest(TestCase):
	
	def test_template_has_non_field_errors(self):
		invalid_data = dict(name='Henrique Bastos', cpf='12345678901')
		response = self.client.post(r('subscriptions:new'), invalid_data)

		self.assertContains(response, '<ul class="errorlist nonfield">')




