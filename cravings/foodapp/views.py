from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import CustomUser, menu, order

def messsignup(request):
    return render(request, "messsignup.html")

def profile(request):
    return render(request, "profile.html")

def mess(request):
    return render(request, "ordertable.html")

def logout(request):
    auth.logout(request)
    return redirect("/login")

def showmenu(request):
    if request.method == "POST":
        items = menu.objects.filter(block = request.user.block)
        quantity = []
        for i in items:
            quantity.append(request.POST[str(i.id)])
        print (quantity)

        last_token = order.objects.latest("token_no").token_no + 1
        print(last_token)

        for i in range(len(quantity)):
            if quantity[i] != 0:
                o = order(user = request.user, token_no = last_token , quantity = quantity[i], item = items[i], total =  int(quantity[i])*items[i].rate)
                print(o.total)
                o.save()
        return redirect("/")

    else:
        print(request.user.block)
        items = menu.objects.filter(block = request.user.block)
        print(items)
        return render(request, "menu/menu.html", {"items": items})



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, f"Welcome, {user.username}")
            print (user.user_type)
            if user.user_type == "S":
                return redirect("/menu")
            else:
                return redirect("/mess")
            
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
        name = request.POST["fname"]
        username = request.POST['username']
        password = request.POST['password']
        repass = request.POST['repass']
        email = request.POST['email']
        number = request.POST['pno']
        regno = request.POST['regno']
        gender = request.POST['gender']
        hostel = request.POST["hostel"]
        
        if CustomUser.objects.filter(username = username).exists():
            messages.info(request, "Username exists")
            return redirect("/signup")
        if CustomUser.objects.filter(regno = regno).exists():
            messages.info(request, "Registration number exists")
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

        if gender == "1":
            user = CustomUser(username = username, email = email, pno = number, regno = regno, gender = "M", block = "M" + hostel)
        else:
            user = CustomUser(username = username, email = email, pno = number, regno = regno, gender = "F", block = "G" + hostel)
        user.set_password(password)
        user.save()
        messages.info(request, "Signup successful")
        return redirect("/login")
    else:
        return render(request, "signup.html")
    
