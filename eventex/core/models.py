
from django.db import models
from django.shortcuts import resolve_url as r

from eventex.core.managers import KindQuerySet, PeriodManager # KindContactManager, EmailContactManager, PhoneContactManager, 


class Speaker(models.Model):
	name = models.CharField('nome', max_length=255)
	slug = models.SlugField('slug')
	photo = models.URLField('foto')
	website = models.URLField('website', blank=True)
	description = models.TextField('descrição', blank=True)

	class Meta:
		verbose_name = 'Palestrante'
		verbose_name_plural = 'Palestrantes'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
	EMAIL = 'E'
	PHONE = 'P'

	KINDS = (
		(EMAIL, 'Email'), 
		(PHONE, 'Telefone')
	)

	speaker = models.ForeignKey('Speaker', verbose_name='Palestrante')
	kind = models.CharField('Tipo', max_length=1, choices=KINDS)
	value = models.CharField('Valor', max_length=255)

	# objects = KindContactManager()
	objects = KindQuerySet.as_manager()

	# objects = models.Manager()
	# emails = EmailContactManager()
	# phones = PhoneContactManager()

	class Meta:
		verbose_name = 'contato'
		verbose_name_plural = 'contatos'

	def __str__(self):
		return self.value


class Talk(models.Model):
	title = models.CharField('Título', max_length=255)
	start = models.TimeField('Inicio', blank=True, null=True)
	description = models.TextField('Descrição', blank=True)
	speakers = models.ManyToManyField('Speaker', verbose_name='Palestrantes', blank=True)

	objects = PeriodManager()

	class Meta:
		ordering = ['start']
		verbose_name = 'palestra'
		verbose_name_plural = 'palestras'

	def __str__(self):
		return self.title


class Course(Talk):
	slots = models.IntegerField()
	objects = PeriodManager()

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'