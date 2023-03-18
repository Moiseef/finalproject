from django.shortcuts import render
from .models import Home_articl
from .models import Home_slide
from .models import Logo
from .models import About_articl
from .models import About_slide
from .models import Title_contact

 
def index(request):
    homeart = Home_articl.objects.all()
    homeslide = Home_slide.objects.all()
    logo = Logo.objects.order_by()[:1]
    return render(request, "realty/index.html", {'homeart': homeart , 'homeslide': homeslide, 'logo': logo})
def about(request):
    aboutart = About_articl.objects.all()
    aboutslide = About_slide.objects.all()
    logo = Logo.objects.order_by()[:1]
    return render(request, "realty/about.html", {'logo': logo, 'aboutart': aboutart, 'aboutslide': aboutslide})
def realty(request):
    logo = Logo.objects.order_by()[:1]
    return render(request, "realty/realty.html", {'logo': logo})    
def contact(request):
    logo = Logo.objects.order_by()[:1]
    ticont = Title_contact.objects.order_by()[:1]
    return render(request, "realty/contact.html", {'logo': logo, 'ticont': ticont})        