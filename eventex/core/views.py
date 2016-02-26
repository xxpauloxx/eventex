
from django.shortcuts import render, HttpResponse, get_object_or_404
from eventex.core.models import Speaker, Talk, Course


def home(request):
	speakers = Speaker.objects.all()
	return render(request, "index.html", {'speakers': speakers})


def speaker_detail(request, slug=None):
	speaker = get_object_or_404(Speaker, slug=slug)
	return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
	"""
	context = {
		'morning_talks': Talk.objects.filter(start__lt='12:00'),
		'afternoon_talks': Talk.objects.filter(start__gte='12:00'),
	}
	"""
	speaker = Speaker(name='Henrique Bastos', slug='henrique-bastos')
	courses = [
		dict(
			title='Título do Curso',
			start='09:00',
			description='Descrição do curso.',
			speakers={'all': [speaker]}
		)
	]

	context = {
		'morning_talks': Talk.objects.at_morning(),
		'afternoon_talks': Talk.objects.at_afternoon(),
		'courses': Course.objects.all(),
	}	
	return render(request, 'core/talk_list.html', context)