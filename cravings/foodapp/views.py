from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import CustomUser

def index(request):
    return render(request, "index.html")


def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, f"Welcome, {user.username}")
            print(user.type)
            if user.type == "hospital":
                return redirect("/userpage")
            else:
                return redirect("/doctor")
            
        elif CustomUser.objects.filter(username = username).exists():
            messages.info(request, "Password does not match")
            return redirect("/login")
        else:
            messages.info(request, "Invalid Username")
            return redirect("/login")

    else:
        return render(request, "login.html")
    
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        repass = request.POST['repass']
        email = request.POST['email']
        number = request.POST['pno']
        regno = request.POST['regno']
        hostel = render.POST["hostel"]
        
        if CustomUser.objects.filter(username = username).exists():
            messages.info(request, "Username exists")
            return redirect("/signup")
        elif CustomUser.objects.filter(email = email).exists():
            messages.info(request, "Email exists")
            return redirect("/signup")
        elif CustomUser.objects.filter(pno = number).exists():
            messages.info(request, "Phone number already registered")
            return redirect("/signup")
        elif password != repass:
            messages.info(request, "Passwords do not match")
            return redirect("/signup")

        user = CustomUser(username = username, email = email, pno = number)
        user.set_password(password)
        user.save()
        messages.info(request, "Signup successful")
        return redirect("/login")
    else:
        return render(request, "signup.html")
    
