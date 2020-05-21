from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Board, Topic, Post
from django import template
from django.contrib.auth.models import Group
from django.core.mail import BadHeaderError, EmailMessage
from django.core.mail import send_mail
from django.conf import settings

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def home(request):
    board = Board.objects.all()
    return render(request, 'home.html', {'board': board})


def dashboard(request):
    boards = Board.objects.all()
    return render(request, 'dashboard.html', {'boards': boards})

def forum(request):
    boards = Board.objects.all()
    return render(request, 'forum.html', {'boards': boards})

def thank(request):
    boards = Board.objects.all()
    return render(request, 'thank.html', {'boards': boards})

def contact(request):
    #check for POST requests on load.
    request.method == 'POST'
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    email = request.POST.get('email')

    if subject and message and email:
        try:
            send_mail(subject= subject,message= message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list = [email],fail_silently  = True,)
        except BadHeaderError:
            return HttpResponse('Invalid header found.') 
        return redirect('thank')

    else:
        #loading contacts.html if no requests
        return render(request, 'contact.html')

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})




def orderdone(request):
    boards = Board.objects.all()
    return render(request, 'orderdone.html', {'boards': boards})

# def order(request):
#     #check for POST requests on load.
#     request.method == 'POST'
#     user = User.objects.first()
#     paquet = request.POST.get('paquet')
#     quantity = request.POST.get('quantity')
#     other = request.POST.get('other')
#     check = request.POST.get('check')

#     if paquet and quantity and check:
#         return redirect('order')

#     else:
        
#         return render(request, 'home.html')

