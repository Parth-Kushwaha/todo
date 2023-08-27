from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from . import forms 

def login_user(request):
    message='message:'
    form=forms.loginForm()
    if request.method=='POST':
        form=forms.loginForm(request.POST)
        if form.is_valid():
            user= authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                message='Login Failed'
    return render(request, 'authentication/login_page.html', context={'form':form, 'message':message})

def signup_user(request):
    form=forms.SignUpForm()
    if request.method=='POST':
        form=forms.SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    return render(request, 'authentication/signup_page.html',context={'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')

