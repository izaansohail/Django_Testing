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
        name = request.POST.get('Name')
        cnic = request.POST.get('cnic')
        address = request.POST.get('Address')
        organization = request.POST.get('Organization')
        contact_number = request.POST.get('Contact_Number')
        checkin = request.POST.get('Check-In')
        checkout = request.POST.get('Check-Out')
        contact_person = request.POST.get('Contact_Person')
        purpose = request.POST.get('Purpose')
        img_location = request.POST.get('Img_lLocation')
        contact = Contact(name=name,cnic = cnic, address=address,
        organization=organization,contact_number=contact_number,checkin=checkin,checkout=checkout,
        contact_person=contact_person,purpose=purpose,img_location=img_location)
        contact.save()
        messages.success(request, 'Your Details have been saved in database.')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")


