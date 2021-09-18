from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
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
   # return HttpResponse('Hello welcome contacts page!!!')