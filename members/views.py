from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SigninForm, SignupForm
from events.models import Event

# Create your views here.

def login_view(request):
    
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('members:home'))
    
    else:
        error = False
        
        if request.method == 'POST':
            form = SigninForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('members:home'))
                else:
                    error = True
        else:
            form = SigninForm()
        
        return render(request, 'members/login.html', locals())

@login_required
def home_view(request):
    user = User.objects.get(id=request.session.get('_auth_user_id'))
    events = user.event_set.all()

    event_exist = True if len(events) >= 0 else False

    return render(request, 'members/home.html', locals())

@login_required(login_url='')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('members:login'))


def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('members:home'))

    else:
        error = False
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['password_conf']:
                    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                    login(request, user)
                    return HttpResponseRedirect(reverse('members:home'))
                else:
                    error = True
            else:
                error = True
        else:
            form = SignupForm()
        
        return render(request, 'members/register.html', locals())
