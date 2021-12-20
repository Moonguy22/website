from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import FeedBackForm, SignupForm, CommentForm
from .utils import message

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product_id = pk
            comment.save()
    return redirect('app:detail', pk=pk)    

def feedback(request):
    form = FeedBackForm(None or request.POST)
    if request.method == 'POST':
        if form.is_valid():
            dict = request.POST.copy()
            dict.pop("csrfmiddlewaretoken")
            message = message.format(**dict)
            print(message)
    return render(request, 'feedback.html', {'form': form})