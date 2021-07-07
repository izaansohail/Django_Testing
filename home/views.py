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
        name = request.POST.get('name')
        address = request.POST.get('address')
        organization = request.POST.get('organization')
        contact_number = request.POST.get('contact_number')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        contact_person = request.POST.get('contact_person')
        purpose = request.POST.get('purpose')
        img_location = request.POST.get('img_location')
        contact = Contact(name=name,address=address,
        organization=organization,contact_number=contact_number,checkin=checkin,checkout=checkout,
        contact_person=contact_person,purpose=purpose,img_location=img_location)
        contact.save()
        messages.success(request, 'Your Details have been saved in database.')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")


