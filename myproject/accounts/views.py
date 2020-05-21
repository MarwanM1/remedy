from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
#from .forms import HomeForm
from .models import Listing
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
        	#print(form.cleaned_data['nom'])
        	#print(form.cleaned_data['prenom'])
        	#print(form.cleaned_data['profession'])
        	#print(form.cleaned_data['check_me_out'])
            
            user = form.save()

            if form.cleaned_data['check_me_out'] == True:   

        	    group = Group.objects.get(name='Volontaires')
        	    user.groups.add(group)
            auth_login(request,user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

