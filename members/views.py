from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import  logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers


from events.models import Event, Guest, Comment
from .models import Message
from .forms import ChangeForm, SendMessageForm

# Create your views here.

@login_required
def home_view(request):
    """
        The function to show the user's dashboard.
    """
    my_events = request.user.event_set.all().order_by('-date')[:4] # les 4 evenemtns les plus proche que l'utilisateur organise
    guest_events = Event.objects.filter(user=request.user).order_by('-date')[:4] # les 4 evenement les plus proches auquel l'utilisateur est inscrit
    messages = request.user.targets.all().order_by('-date')[:4] # les 4 derniers message que l'utilisateurs a recu
    responses = Comment.objects.exclude(response_to = None).order_by('-date')
    com_reponses = []
    for response in responses:
        if len(com_reponses) > 3:
            break
        elif response.response_to.author == request.user:
            com_reponses.append(response)

    return render(request, 'members/home.html', locals())

@login_required
def profil_view(request):
    """
        The function to show the user's profil.
    """
    return render(request, 'members/profil.html', locals())

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

@login_required
def getMessage(request):
    messages = serializers.serialize('json', request.user.targets.filter(author=User.objects.get(pk=request.GET['author_id'])).order_by('date'))
    return JsonResponse(messages, safe=False)

@login_required
def message_view(request):
    messages = request.user.targets.all().order_by('date')
    messages_sent = request.user.message_set.all().order_by('date')
    targets = {}
    for message in messages_sent:
        targets_tmp = message.target.all()
        for target in targets_tmp:
            if not target in targets:
                targets[target] = message.date
            elif targets[target] < message.date:
                targets[target] = message.date

    for message in messages:
        author = message.author
        if not author in targets:
            targets[author] = message.date
        elif targets[author] < message.date:
            targets[author] = message.date

    targets = sorted(targets.items(), key=lambda x: x[1], reverse=True)
    form = SendMessageForm()
    return render(request, 'members/message.html', locals())


@login_required
def send_message(request):
    """
        The function to send a message, there is no template link to the function.
    """
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            targets = form.cleaned_data['target'].split(', ')
            message = Message(
                content=form.cleaned_data['content'],
                author = request.user,
            )
            message.save()
            for target in targets:
                message.target.add(User.objects.get(username=target))
            message.save()

            form = SendMessageForm(initial={'target': form.cleaned_data['target']})
        
        if request.POST['author_id']:
            message = Message(
                content=request.POST['content'],
                author = request.user,
            )
            message.save()
            author_id = request.POST['author_id'].split(', ')
            for auth in author_id:
                message.target.add(User.objects.get(pk=auth))
            message.save()
    return JsonResponse("ok", safe=False)
