from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import CustomUser, menu, order
import datetime

def messsignup(request):
    return render(request, "messsignup.html")

def profile(request):
    return render(request, "user-pages/profile.html")

def invoice(request):
    d = order.objects.all().values_list("total")
    for i in d:
        subtotal=subtotal+i
    con=0.075*subtotal    
    return render(request, "invoice.html")

def mess_home(request):
    if request.method == "POST":
        items = request.POST.getlist("chk[]")
        items = [int(x) for x in items]
        del_items = menu.objects.filter(pk__in = items)
        del_items.delete()
    items = menu.objects.filter(block = request.user.block)
    print(items)
    return render(request, "mess-pages/mess-menu.html", context = {"items": items})

def pending_orders(request):
    if request.method == "POST":
        token = request.POST['token1']
        orders = order.objects.filter(token_no = token)
        for i in orders:
            i.ready = True
            i.save()
        return redirect("/mess_orders")
    
    else:
        orders = order.objects.filter(block = request.user.block, valid = True, ready = False)
        return render(request, "mess-pages/ordertable.html", context={"orders": orders, "title": "Pending Orders", "button":"Ready", "disabled": "", "action":"mess"})
    
def ready_orders(request):
    if request.method == "POST":
        token = request.POST['token1']
        orders = order.objects.filter(token_no = token)
        for i in orders:
            i.valid = False
            i.save()
        return redirect("/ready_orders")
    
    else:
        orders = order.objects.filter(block = request.user.block, valid = True, ready = True)
        return render(request, "mess-pages/ordertable.html", context={"orders": orders, "title": "Ready Orders", "button": "Deliver","disabled": "", "action":"ready"})
    
def delivered_orders(request):
    orders = order.objects.filter(block = request.user.block, valid = False)
    return render(request, "mess-pages/ordertable.html", context={"orders": orders, "title": "Delivered Orders", "disabled": "disabled", "button":"delivered", "action":"delivered"})
    
def logout(request):
    auth.logout(request)
    return redirect("/login")

def showmenu(request):
    if request.method == "POST":
        items = menu.objects.filter(block = request.user.block, is_available = True)
        print(items)
        quantity = []
        for i in items:
            quantity.append(request.POST[str(i.id)])
        print (quantity)

        cur_token = order.objects.latest("token_no").token_no + 1

        for i in range(len(quantity)):
            if quantity[i] != "0":
                o = order(user = request.user, token_no = cur_token , quantity = quantity[i], item = items[i], total =  int(quantity[i])*items[i].rate, block = request.user.block)
                o.save()

        cur_orders = order.objects.filter(token_no = cur_token)

        total = 0
        for i in cur_orders:
            total += i.total

        dic = {"orders": cur_orders, "total":total, "sub": total*0.075, "grand": total*1.075, "token":cur_token, "date_time": datetime.datetime.now().strftime("%d/%m/%Y \n %H:%M:%S")}
        return render(request, "user-pages/invoice.html", context=dic)

    else:
        veg = menu.objects.filter(block = request.user.block, cat = "Veg", is_available = True)
        nonveg = menu.objects.filter(block = request.user.block, cat = "Non veg", is_available = True)
        user_mess = CustomUser.objects.filter(user_type = "M", block = request.user.block)
        return render(request, "user-pages/menu.html", {"veg": veg, "nonveg": nonveg, "mess": user_mess})



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
                return redirect("/user_home")
            else:
                return redirect("/mess_home")
            
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
                return redirect("/mess_home")
        else:
            return render(request, 
                          "login.html")
        
def user_home(request):
    return render(request, "user-pages/home-page.html")
        
    
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
    
def add_item(request):
    if request.method == "POST":
        name = request.POST["name"]
        rate = request.POST["mrp"]
        cat = request.POST["cat"]
        item = menu(block = request.user.block, item = name, rate = rate, cat = cat)
        item.save()
        return redirect("/mess_home")
    
    return render(request, "mess-pages/additem.html")

def about(request):
    return render(request, "user-pages/about.html")

def orderhistory(request):
    history = order.objects.filter(user = request.user).order_by("-id")[:20]
    for i in history:
        i.book_time = i.book_time.strftime("%d/%m/%Y \n %H:%M:%S")
    print(history)
    return render(request, "user-pages/orderhistory.html", context={"history": history})

def about_mess(request):
    return render(request, "mess-pages/about-mess.html")
