from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from home.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate , login 
from django.contrib.auth.decorators import login_required


# Create your views here.       
#password is Sachin$$$***000
@login_required(login_url="/login")
def index(request):
    print(request.user.is_authenticated)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    #return HttpResponse('Hello welcome to sachin world!!!')
@login_required(login_url="/login")
def about(request):
    return render(request,'about.html')
    # return HttpResponse('Hello welcome about page!!!')
@login_required(login_url="/login")
def services(request):
    return render(request,'services.html')
    #return HttpResponse('Hello welcome services page!!!')
@login_required(login_url="/login")
def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent.')
    return render(request,'contact.html')
@login_required(login_url="/login")
def employe(request):
    return render(request,'employe.html')
   # return HttpResponse('Hello welcome contacts page!!!)'
@login_required(login_url="/login")
def employe_planning(request):

    if request.method=="POST":
        print(request.POST)
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        C_name=request.POST.get('C_name')
        R_time=request.POST.get('R_time')
        loc=request.POST.get('location')
        uom=request.POST.get('uom')
        quantity=request.POST.get('quantity')
        rate=request.POST.get('rate')
        value=request.POST.get('value')
        planning = Planning(name=name, desc=desc, C_name=C_name, time=R_time, loc=loc, uom=uom, quantity=quantity,rate=rate,value=value,date=datetime.today())
        planning.save()
        messages.success(request, "Target created successfully!")
    return render(request,'planning.html')

@login_required(login_url="/login")
def employe_viewplanning(request):
    view_planning = Planning.objects.all().order_by("uom")
    user_wiseplanning=[]
    if not request.user.is_superuser:
        for i in view_planning:
            if i.name.lower()==request.user.username.lower():
                user_wiseplanning.append(i)
        view_planning=user_wiseplanning                                                                 
    print(view_planning,'jjjjjjjjjj')
    return render(request,'viewplanning.html',locals())

# login & logoutx


def login(request):
    if request.method=="Post":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if the user has entered the correct credential
        user = authenticate(username=username, password=password)
        if user is not None:
          # A backend authenticated the credentials
          login(user)
          return redirect("/")
        else:
          # No backend authenticated the credentials
          return render(request,'login.html')

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
   