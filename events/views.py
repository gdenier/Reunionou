import uuid

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.models import User

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