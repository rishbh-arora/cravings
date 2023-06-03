from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import CustomUser, menu, order
import datetime

def messsignup(request):
    return render(request, "messsignup.html")

def profile(request):
    return render(request, "profile.html")

def invoice(request):
    d = order.objects.all().values_list("total")
    for i in d:
        subtotal=subtotal+i
    con=0.075*subtotal    
    return render(request, "invoice.html")

def mess(request):
    print(request.user.block)
    nos = list(set(order.objects.filter(valid = True, block = request.user.block).values_list("token_no").distinct()))
    tokens = []
    for i in nos:
        tokens.append(i[0])
    print(tokens)
    users = order.objects.filter(valid = True, block = request.user.block).values_list("user").distinct()
    orders = order.objects.filter(valid = True, block = request.user.block)

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

        cur_token = order.objects.latest("token_no").token_no + 1

        for i in range(len(quantity)):
            if quantity[i] != 0:
                o = order(user = request.user, token_no = cur_token , quantity = quantity[i], item = items[i], total =  int(quantity[i])*items[i].rate, block = request.user.block)
                o.save()

        cur_orders = order.objects.filter(token_no = cur_token)

        total = 0
        for i in cur_orders:
            total += i.total

        dic = {"orders": cur_orders, "total":total, "sub": total*0.075, "grand": total*1.075, "token":cur_token, "date_time": datetime.datetime.now().strftime("%d/%m/%Y \n %H:%M:%S")}
        return render(request, "invoice.html", context=dic)

    else:
        print(request.user.block)
        veg = menu.objects.filter(block = request.user.block, cat = "Veg")
        nonveg = menu.objects.filter(block = request.user.block, cat = "Non veg")
        return render(request, "menu/menu.html", {"veg": veg, "nonveg": nonveg})



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
        if request.user.is_authenticated:
            if request.user.user_type == "S":
                return redirect("/menu")
            else:
                return redirect("/mess")
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
            user = CustomUser(first_name = name, username = username, email = email, pno = number, regno = regno, gender = "M", block = "M" + hostel, user_type = "S")
        else:
            user = CustomUser(first_name = name, username = username, email = email, pno = number, regno = regno, gender = "F", block = "G" + hostel, user_type = "S")
        user.set_password(password)
        user.save()
        messages.info(request, "Signup successful")
        return redirect("/login")
    else:
        return render(request, "signup.html")
    

def messsignup(request):
    if request.method == "POST":
        name = request.POST["fname"]
        username = request.POST['username']
        password = request.POST['password']
        repass = request.POST['repass']
        email = request.POST['email']
        number = request.POST['pno']
        gender = request.POST['gender']
        hostel = request.POST["hostel"]
        
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

        if gender == "1":
            user = CustomUser(first_name = name, username = username, email = email, pno = number, gender = "M", block = "M" + hostel, user_type = "M")
        else:
            user = CustomUser(first_name = name, username = username, email = email, pno = number, gender = "F", block = "G" + hostel, user_type = "M")
        user.set_password(password)
        user.save()
        messages.info(request, "Signup successful")
        return redirect("/login")
    else:
        return render(request, "messsignup.html")
    
