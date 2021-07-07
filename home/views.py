from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'homescreen.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
     return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        contact = Contact(email=email , password=password)
        contact.save()
        messages.success(request, 'Your Details have been saved in database.')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")


