from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import datetime

# Create your views here.
def Home(request):
    data = 0
    error = ""
    user=""
    try:
        user = User.objects.get(username=request.user.username)
    except:
        pass
    try:
        data = Bidder.objects.get(user=user)
        if data:
            error = "pat"
            return redirect('profile1')
    except:
        pass
    try:
        data = Auction_User.objects.get(user=user)
        return redirect('trainer_home')
    except:
        pass
    d = {'error':error,'data':data}
    return render(request, 'carousel.html',d)


def new():
    status = Status.objects.get(status="pending")
    new_pro = Product.objects.filter(status=status)
    return new_pro


def About(request):
    return render(request, 'about.html')


def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        sign = ""
        if user:
            try:
                sign = Bidder.objects.get(user=user)
            except:
                pass
            if sign:
                login(request, user)
                error = "pat"
            else:
                login(request, user)
                error = "pat1"
        else:
            error="not"
    d = {'error': error}
    return render(request, 'login.html', d)


def Login_Admin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "yes"
        else:
            error = "not"

    d = {'error': error}
    return render(request, 'loginadmin.html', d)

def Signup_User(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        con = request.POST['contact']
        add = request.POST['add']
        d2 = request.POST['dob']
        reg = request.POST['reg']
        i = request.FILES['image']
        user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
        mem = Member_fee.objects.get(fee="Unpaid")
        if reg == "Bidder":
            sign = Bidder.objects.create(membership=mem,user=user,contact=con,address=add,dob=d2,image=i)
        else:
            sign = Auction_User.objects.create(membership=mem,user=user,contact=con,address=add,dob=d2,image=i)
        error = True
    d = {'error':error}
    return render(request,'signup.html',d)


def Logout(request):
    logout(request)
    return redirect('home')

