from django.shortcuts import render
from .models import Home_articl
from .models import Home_slide
from .models import Logo
from .models import About_articl
from .models import About_slide
from .models import Title_contact
from .models import Call_us
from .models import Social_us
from .models import Email_us
from .models import Contact_form
from .models import Product
from .models import Image

 
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
    card = Product.objects.all()
    return render(request, "realty/realty.html", {'logo': logo, 'card': card})    
def contact(request):
    logo = Logo.objects.order_by()[:1]
    ticont = Title_contact.objects.order_by()[:1]
    call_us = Call_us.objects.order_by()[:1]
    email_us = Email_us.objects.order_by()[:1]
    social_us = Social_us.objects.order_by()[:1]
    cont_form = Contact_form.objects.order_by()[:1]
    return render(request, "realty/contact.html", {'logo': logo, 'ticont': ticont, 'call_us': call_us, 'email_us': email_us, 'social_us': social_us, 'cont_form': cont_form})        