from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView

from .models import Events, Participants
from .forms import ParticipantForm

from datetime import date
# index, schedule_controller, wiki_controller, categories_controller

def index(request: HttpRequest):
    return render(request, 'badm/index.html')

def wiki_controller(request: HttpRequest):
    return render(request, 'badm/wiki.html')

def categories_controller(request: HttpRequest):
    return render(request, 'badm/categories.html')

def schedule_controller(request: HttpRequest):
    events = Events.objects.filter(date__gte=date.today()).order_by('date')
    context = {
        'events': events,
    }
    return render(request, 'badm/schedule.html', context)




class AddParticipantView(CreateView):
    model = Participants
    form_class = ParticipantForm
    template_name = 'badm/form.html'
    success_url = reverse_lazy('home')

    
    

