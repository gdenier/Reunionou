from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import  logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from events.models import Event

# Create your views here.

@login_required
def home_view(request):
    user = User.objects.get(id=request.session.get('_auth_user_id'))
    events = user.event_set.all()

    event_exist = True if len(events) >= 0 else False

    return render(request, 'members/home.html', locals())

@login_required(login_url='')
def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès")
    return HttpResponseRedirect(reverse('members:login'))

