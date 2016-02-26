
from django.db import models 


"""
class EmailContactManager(models.Manager):
	def get_queryset(self):
		qs = super().get_queryset()
		qs = qs.filter(kind=self.model.EMAIL)
		return qs


class PhoneContactManager(models.Manager):
	def get_queryset(self):
		qs = super().get_queryset()
		qs = qs.filter(kind=self.model.PHONE)
		return qs
"""

class KindQuerySet(models.QuerySet):
	def emails(self):
		return self.filter(kind=self.model.EMAIL)

	def phones(self):
		return self.filter(kind=self.model.PHONE)


class PeriodManager(models.Manager):
	MIDDAY = '12:00'

	def at_morning(self):
		return self.filter(start__lt=self.MIDDAY)

	def at_afternoon(self):
		return self.filter(start__gte=self.MIDDAY)

"""
class KindContactManager(models.Manager):

	def get_queryset(self):
		return KindQuerySet(self.model, using=self._db)

	def emails(self):
		# return self.filter(kind=self.model.EMAIL)
		return self.get_queryset().emails()

	def phones(self):
		# return self.filter(kind=self.model.PHONE)
		return self.get_queryset().phones()
"""