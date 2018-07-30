from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import SigninForm, SignupForm

# Create your views here.

def Home_view(request):
    """
        The function to show the home page of the website
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('members:home'))
    return render(request, 'index/home.html')

def login_view(request):
    """
        The function to authenticate the user. And to redirect him to his dashboard.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('members:home'))
    else:
        error = False

        if request.method == 'POST':
            form = SigninForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('members:home'))
                else:
                    error = True
                    messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
        else:
            form = SigninForm()
        
    return render(request, 'index/login.html', locals())

def register_view(request):
    """
        The function to register the user. And to redirect him to the login page.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('members:home'))
    else:
        error = False
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['password_conf']:
                    try:
                        test = User.objects.get(email=form.cleaned_data['email'])
                        messages.error(request, "Email déjà pris")
                    except User.DoesNotExist:
                        user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                        # login(request, user)
                        messages.success(request, "Votre compte a bien été crée")
                        return HttpResponseRedirect(reverse('index:login'))
                    except IntegrityError:
                        messages.error(request, "Identifiant déjà pris")

                else:
                    messages.error(request, "Mot de passe ne correpondent pas")
            else:
                messages.error(request, "Votre compte n'a pas pu être crée")
        else:
            form = SignupForm()
    
    return render(request, 'index/register.html', locals())

 
def e_handler404(request):
    context = RequestContext(request)
    response = render_to_response('index/error404.html', context)
    response.status_code = 404
    return response
 
 
def e_handler500(request):
    context = RequestContext(request)
    response = render_to_response('index/error500.html', context)
    response.status_code = 500
    return response