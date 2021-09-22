from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from home.models import *
from django.contrib import messages

# Create your views here.
#password is Sachin$$$***000
def index(request):
    return render(request,'index.html')
    #return HttpResponse('Hello welcome to sachin world!!!')
def about(request):
    return render(request,'about.html')
    # return HttpResponse('Hello welcome about page!!!')
def services(request):
    return render(request,'services.html')
    #return HttpResponse('Hello welcome services page!!!')
def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent.')
    return render(request,'contact.html')
def employe(request):
    return render(request,'employe.html')
   # return HttpResponse('Hello welcome contacts page!!!)'

def employe_planning(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        C_name=request.POST.get('C_name')
        R_time=request.POST.get('R_time')
        loc=request.POST.get('location')
        quantity=request.POST.get('quantity')
        rate=request.POST.get('rate')
        value=request.POST.get('value')
        planning = Planning(name=name, desc=desc, C_name=C_name, time=R_time, loc=loc, quantity=quantity,rate=rate,value=value,date=datetime.today())
        planning.save()

    return render(request,'planning.html')

def employe_viewplanning(request):
    view_planning = Planning.objects.all()
    print(view_planning,'jjjjjjjjjj')
    return render(request,'viewplanning.html',locals())

#login & logout

# def login(request):
#     return render(request,'login.html')

# def logout(request):
#     return render(request,'logout.html')
   