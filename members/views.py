from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import  logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from events.models import Event
from .forms import ChangeForm

# Create your views here.

@login_required
def home_view(request):
    """
        The function to show the user's dashboard.
    """
    events = request.user.event_set.all()

    event_exist = True if len(events) >= 0 else False

    return render(request, 'members/home.html', locals())

@login_required(login_url='')
def logout_view(request):
    """
        The function to logout the user and to redirect him to the login page.
    """
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès")
    return HttpResponseRedirect(reverse('index:login'))

@login_required
def change_view(request):
    """
        The function to change user's information.

        Firstly:
        The function create the form with actual data and send it to the template.

        Secondly:
        The function take data and modify actual value with the right format.
    """
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_conf']:
                request.user.username = form.cleaned_data['username']
                if form.cleaned_data['password'] != '******':
                    request.user.password = form.cleaned_data['password']
                request.user.last_name = form.cleaned_data['last_name']
                request.user.first_name = form.cleaned_data['first_name']
                request.user.email = form.cleaned_data['email']

                request.user.save()

                messages.success(request, "Vos informations ont bien été mise à jour")
                return HttpResponseRedirect(reverse('members:home'))
    else:
        form = ChangeForm(initial={
            'username': request.user.username,
            'password': "******",
            'password_conf': "******",
            'last_name': request.user.last_name,
            'first_name': request.user.first_name,
            'email': request.user.email,
        })

    return render(request, 'members/change.html', locals())