from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HomeForm
from django import template
from django.contrib.auth.models import Group
from django.conf import settings
from django import forms
# Create your views here.

def order(request):
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            return redirect('orderdone')
    else:
        form = HomeForm()
    return render(request, 'home.html', {'form': form})
    