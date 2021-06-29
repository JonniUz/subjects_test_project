from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import UserRegisterForm


def login(request):
    return render(request, 'registration/login.html')


def signup(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save()
            messages.error(request,f'{username} have been signed up! Now you are able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})
