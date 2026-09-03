from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm,ProfileForm,PostForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Post

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

@login_required
def home(request):
    posts=Post.objects.all().order_by("-created_at")
    return render(request, "accounts/home.html",{"posts":posts})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    if request.method == "POST":
        form=ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form=ProfileForm(instance=request.user.profile)
    return render(request,"accounts/profile.html",{"form":form})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("home")
    else:
        form=PostForm()
    return render(request,"accounts/create_post.html",{"form":form})

@login_required
def like_post(request,post_id):
    post=Post.objects.get(id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect("home")