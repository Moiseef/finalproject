from django.shortcuts import render
from .models import Home_articl
from .models import Home_slide

 
def index(request):
    homeart = Home_articl.objects.all()
    homeslide = Home_slide.objects.all()
    return render(request, "realty/index.html", {'homeart': homeart , 'homeslide': homeslide})
def about(request):
    return render(request, "realty/about.html")
def realty(request):
    return render(request, "realty/realty.html")    
def contact(request):
    return render(request, "realty/contact.html")        