
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView 

from eventex.core.models import Speaker, Talk, Course


home = ListView.as_view(template_name='index.html', model=Speaker)


"""
def home(request):
	speakers = Speaker.objects.all()
	return render(request, "index.html", {'speakers': speakers})
"""

def speaker_detail(request, slug=None):
	speaker = get_object_or_404(Speaker, slug=slug)
	return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
	at_morning = list(Talk.objects.at_morning()) + list(Course.objects.at_morning())
	at_morning.sort(key=lambda o: o.start)

	at_afternoon = list(Talk.objects.at_afternoon()) + list(Course.objects.at_afternoon())
	at_afternoon.sort(key=lambda o: o.start)

	context = {
		'morning_talks': at_morning,
		'afternoon_talks': at_afternoon,
	}	
	return render(request, 'core/talk_list.html', context)