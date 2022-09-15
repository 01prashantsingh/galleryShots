
from django.shortcuts import render
from .models import  Contact
from math import ceil

# Create your views here.


def home(request):
    
    return render(request, 'home.html')




def about(request):
    return render(request, 'about.html')


def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        zip = request.POST.get('zip', '')
        state = request.POST.get('state', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email,state=state, city=city,zip=zip, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})


def service(request):
     return render(request,"service.html")

def gallery(request):
     return render(request,"gallery.html")

