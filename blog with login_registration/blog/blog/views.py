from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import  SignUpForm
from django.contrib.auth.models import User

#from django.contrib.auth.forms import UserCreationForm


def home(request):
   return render(request, 'home.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('/login')
    form = SignUpForm()
    return render(request, 'registration/signup.html',{'signup_form':form}) #other



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'thankyou.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'registration/article_list.html') #other


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')