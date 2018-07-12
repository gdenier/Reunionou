from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def Home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('members:home'))
    return render(request, 'index/home.html')