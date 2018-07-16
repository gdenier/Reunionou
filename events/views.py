import uuid
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType

from .forms import NewForm, InvitForm, CommentForm
from index.forms import SignupForm
from .models import Event, Guest, Comment

# Create your views here.

#-- créer une permission pour chaque event pour qu'un groupe puisse le modifier (auteur + personel autorise)
@login_required
def New_view(request):
    error = False

    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            token_tmp = str(uuid.uuid4()).replace("-", "")
            event = Event(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                date=form.cleaned_data['date'],
                token=token_tmp,
                author=request.user,
                public=0,
                addresse=form.cleaned_data['addresse']
            )
            event.save()
            content_type = ContentType.objects.get(app_label='events', model='Event')
            permission = Permission.objects.create(
                codename='change_event_{}'.format(event.token),
                name='changer l\'évènement "{}"'.format(event.token),
                content_type=content_type,
            )
            request.user.user_permissions.add(permission)
            return HttpResponseRedirect(reverse('members:home'))

    else:
        form = NewForm()
    
    return render(request, 'events/new.html', locals())

def Detail_view(request, token):

    event = get_object_or_404(Event, token=token)
    inscrits = event.guest_set.all()
    comments = event.comment_set.all().order_by('date')
    comments = trie_comment(comments)
    form = CommentForm()

    if request.user.is_authenticated:
        
        if event.author == request.user:
            return render(request, 'events/detail_author.html', locals())
        
        else:
            return render(request, 'events/detail_public.html', locals())
    
    else:
        return render(request, 'events/detail_public.html', locals())    

@login_required
def Change_view(request, token):
    if request.user.has_perm("events.change_event_{}".format(token)):
        event = get_object_or_404(Event, token=token, auteur_id=request.user.id)

        error = False

        if request.method == 'POST':
            form = NewForm(request.POST)
            if form.is_valid():

                event.title=form.cleaned_data['title']
                event.description=form.cleaned_data['description']
                event.date=form.cleaned_data['date']
                event.addresse=form.cleaned_data['addresse']

                event.save()

                return HttpResponseRedirect(reverse('events:detail', args=[event.token]))

        else:
            form = NewForm(initial={
                'title': event.title,
                'description': event.description,
                'date': event.date,
                'addresse': event.addresse,
            })
        
        return render(request, 'events/change.html', locals())
    else:
        return HttpResponseForbidden()

@login_required
def List_view(request):
    events = Event.objects.filter(public=1)
    return render(request, 'events/list.html', locals())


def Register_view(request, token, args='default'):
    event = Event.objects.get(token=token)
    if request.user.is_authenticated:
        
        #inscription avec info perso du compte
        if args == 'accept':
            
            guest = Guest(
                last_name=request.user.last_name,
                first_name=request.user.first_name,
                email=request.user.email,
                event=event,
                user=request.user,
            )
            guest.save()

            return HttpResponseRedirect(reverse('events:detail', args=[token]))

        return render(request, 'events/register_user.html', locals()) #a faire en fenetre "pop-up" plus tard je pense

    else:
        #si oui -> création puis inscription
        if args == 'create':
            if request.method == 'POST':
                form = SignupForm(request.POST)
                if form.is_valid():
                    if form.cleaned_data['password'] == form.cleaned_data['password_conf']:
                        user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                        login(request, user)

                        guest = Guest(
                            last_name=user.first_name,
                            first_name=user.first_name,
                            email=user.email,
                            event=event,
                            user=request.user,
                        )
                        guest.save()
                        
                        return HttpResponseRedirect(reverse('events:detail', args=[token]))
            else:
                form = SignupForm()
            return render(request, 'events/create_user.html', locals())

        #si non -> inscription avec compte temporaire et accès qu'a cet évènement
        if args == 'invit':
            if request.method == 'POST':
                form = InvitForm(request.POST)
                if form.is_valid():
                    #if form.cleaned_data['password'] == form.cleaned_data['password_conf']:
                    guest = Guest(
                        last_name=form.cleaned_data['last_name'],
                        first_name=form.cleaned_data['first_name'],
                        age=form.cleaned_data['age'],
                        email=form.cleaned_data['email'],
                        password=make_password(form.cleaned_data['password'], '100000'),
                        event=event,
                    )
                    guest.save()

                    return HttpResponseRedirect(reverse('events:detail', args=[token]))
            else:
                form = InvitForm()
            return render(request, 'events/create_invit.html', locals())
        
        #demande si création
        return render(request, 'events/register.html', locals())

@login_required
def Comment_view(request, token):
    if request.method == 'POST':
        comment = Comment()
        if request.POST.get('father'):
            comment.author=request.user,
            comment.core=request.POST.get('core'),
            comment.event=Event.objects.get(token=token),
            comment.response_to=Comment.objects.get(id=request.POST.get('father'))
            comment.save()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment(
                    author=request.user,
                    core=form.cleaned_data['core'],
                    event=Event.objects.get(token=token)
                )
                comment.save()
            else:
                return HttpResponseRedirect(reverse('events:detail', args=[token]))

        content_type = ContentType.objects.get(app_label='events', model='Comment')
        permission = Permission.objects.create(
            codename='edit_comment_{}'.format(comment.id),
            name='Editer le commentaire "{}"'.format(comment.id),
            content_type=content_type,
        )
        request.user.user_permissions.add(permission)

        permission = Permission.objects.create(
            codename='delete_comment_{}'.format(comment.id),
            name='Supprimer le commentaire "{}'.format(comment.id),
            content_type=content_type,
        )
        Event.objects.get(token=token).author.user_permissions.add(permission)
        request.user.user_permissions.add(permission)
       
    return HttpResponseRedirect(reverse('events:detail', args=[token]))

def trie_comment(comments, trie=None):
    comments_bis = []
    for comment in comments:
        if comment.response_to == None:
            comments_bis.append(comment)
            for comment_2 in comments:
                if comment_2.response_to == comment:
                    comments_bis.append(comment_2)
    return comments_bis

def Comment_Edit_view(request, token, comment_id):
    if request.user.has_perm("events.edit_comment_{}".format(comment_id)):
        if request.method == 'POST':
            com = Comment.objects.get(id=comment_id)
            com.core = request.POST['core']
            com.edited = str(datetime.now())
            com.save()
            return HttpResponseRedirect(reverse('events:detail', args=[token]))
        return HttpResponseRedirect(reverse('events:detail', args=[token]))
    else:
        return HttpResponseForbidden()

@login_required
def Delete_com_view(request, token, comment_id):
    if request.user.has_perm("events.delete_comment_{}".format(comment_id)):
        comment = Comment.objects.get(pk=comment_id)
        comment.deleted = True
        comment.save()
        return HttpResponseRedirect(reverse('events:detail', args=[token]))
    else:
        return HttpResponseForbidden()