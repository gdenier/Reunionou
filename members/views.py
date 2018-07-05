from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm, SigninForm

# Create your views here.

def login_view(request):
    error = False
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('members:home'))
            else:
                error = True
    else:
        form = LoginForm()
    
    return render(request, 'members/login.html', locals())

def home_view(request):
    username = request.session.get('_auth_user_id')
    return render(request, 'members/home.html', locals())

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('members:login'))

def signin_view(request):
    error = False
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('members:home'))
        else:
            error = True
    else:
        form = SigninForm()
    
    return render(request, 'members/signin.html', locals())
