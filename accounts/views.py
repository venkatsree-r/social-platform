from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def hello(request):
    return HttpResponse("Hello from Social Platform!")

def signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=SignUpForm()
    return render(request,"accounts/signup.html",{"form": form})

def login_view(request):
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect ("home")
    else:
        form=AuthenticationForm()
    return render(request,"accounts/login.html",{"form":form})

def home(request):
    return render(request, "accounts/home.html")