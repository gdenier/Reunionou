import uuid

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .forms import NewForm
from .models import Event

# Create your views here.

def New_view(request, user_id):
    
    if User.objects.filter(id=request.session.get('_auth_user_id')).exists():
        
        error = False

        if request.method == 'POST':
            form = NewForm(request.POST)
            if form.is_valid():
                token_tmp = str(uuid.uuid4()).replace("-", "")
                event = Event(
                    titre=form.cleaned_data['titre'],
                    description=form.cleaned_data['description'],
                    date=form.cleaned_data['date'],
                    token=token_tmp,
                    auteur_id=user_id,
                    adresse=form.cleaned_data['adresse']
                )
                event.save()
                return HttpResponseRedirect(reverse('members:home'))

        else:
            form = NewForm()
        
        return render(request, 'events/new.html', locals())
    
    else:
        return HttpResponseForbidden()

def Detail_view(request, event_id):

    if User.objects.filter(id=request.session.get('_auth_user_id')).exists():
        
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'events/detail.html', locals())
    
    else:
        return HttpResponseForbidden()

def Change_view(request, event_id):
    if User.objects.filter(id=request.session.get('_auth_user_id')).exists():
        
        event = get_object_or_404(Event, id=event_id, auteur_id=request.session.get('_auth_user_id'))

        error = False

        if request.method == 'POST':
            form = NewForm(request.POST)
            if form.is_valid():

                event.titre=form.cleaned_data['titre']
                event.description=form.cleaned_data['description']
                event.date=form.cleaned_data['date']
                event.adresse=form.cleaned_data['adresse']

                event.save()

                return HttpResponseRedirect(reverse('events:detail', args=[event.id]))

        else:
            form = NewForm(initial={
                'titre': event.titre,
                'description': event.description,
                'date': event.date,
                'adresse': event.adresse,
            })
        
        return render(request, 'events/change.html', locals())

    else:
        return HttpResponseForbidden()