from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "homebase.html")

def index2(request):
    return render(request, "homepage2.html")

def profile(request):
    return render(request, "profilepage.html")

def cards(request):
    return render(request, "cards.html")

def login_form(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('./index2.html')
        
        else:
            return render(request, "login.html")
    
    else:
        return render(request, "login.html")
    
def join_form(request):
    if request.method=="POST":
        username=request.POST["username"]
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, "./signup.html", 
                {
                    "eror":"username kullanılıyor", 
                    "username":username,
                    "email":email,
                    "first_name":first_name,
                    "last_name":last_name
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "./signup.html", 
                {
                    "eror":"username kullanılıyor", 
                    "username":username,
                    "email":email,
                    "first_name":first_name,
                    "last_name":last_name
                })
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    return redirect("./otp.html")
        else:
            return render(request, "./signup.html", 
            {
                "eror":"parola eşleşmiyor",
                "username":username,
                "email":email,
                "first_name":first_name,
                "last_name":last_name
            })
    return render(request, "./signup.html")

def logout(request):
    return redirect('./login.html')

def otp(request):
    return render(request, "otp.html")

def heart(request):
    return render(request, "heart.html")