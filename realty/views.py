from ctypes.wintypes import HINSTANCE
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, UpdateView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import ProductForm
from .forms import ImageForm
from django.contrib import messages
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
from .models import AboutSlideDown
from .models import ReviewMy
from .models import News_articl
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import SubscribForm
from .forms import ReviewForm


def index(request):
    homeart = Home_articl.objects.all()
    homeslide = Home_slide.objects.all()
    logo = Logo.objects.order_by()[:1]

    if request.method == "POST":
        form_sub = SubscribForm(request.POST)        
        if form_sub.is_valid():
            form_sub.save()
            messages.success(request, "You subscribed!")
            return HttpResponseRedirect("/") 
        else:
            messages.success(request, "Error!")
            return HttpResponseRedirect("/") 
    else:
        form_sub = SubscribForm()
    return render(request, "realty/index.html", {'homeart': homeart, 'homeslide': homeslide, 'logo': logo, 'form_sub': form_sub})


def about(request):
    aboutart = About_articl.objects.all()
    aboutslide = About_slide.objects.all()
    downslide = AboutSlideDown.objects.all()
    logo = Logo.objects.order_by()[:1]
    review = ReviewMy.objects.all()
    
    if request.method == "POST":
        form_rev = ReviewForm(request.POST, request.FILES)       
        if form_rev.is_valid():
            form_rev.save()
            messages.success(request, "Your review has been sent!")
            return HttpResponseRedirect("/about")  
    else:
         form_rev = ReviewForm()
    return render(request, "realty/about.html", {'logo': logo, 'aboutart': aboutart, 'aboutslide': aboutslide, 'downslide': downslide, 'review': review, 'form_rev': form_rev})


def realty(request):
    logo = Logo.objects.order_by()[:1]
    card = Product.objects.all()

    # Paginator
    paginator = Paginator(card, 3)
    page_number = request.GET.get('page')
    posts_of_the_page = paginator.get_page(page_number)
    list = [i for i in range(1,paginator.num_pages+1)]


    return render(request, "realty/realty.html", {'logo': logo, 'card': card, 'posts_of_the_page': posts_of_the_page, 'list': list})


def contact(request):
    logo = Logo.objects.order_by()[:1]
    ticont = Title_contact.objects.order_by()[:1]
    call_us = Call_us.objects.order_by()[:1]
    email_us = Email_us.objects.order_by()[:1]
    social_us = Social_us.objects.order_by()[:1]
    cont_form = Contact_form.objects.order_by()[:1]

    if request.method == "POST":
        message = request.POST['message'] + ' ' + request.POST['email'] + ' ' + request.POST['phone']
        name = request.POST['name']
        send_mail(
        name, 
        message, 
        'settings.EMAIL_HOST_USER',
        ['moiseef@yahoo.com'],
        fail_silently=False)
        messages.success(request, "Your message has been sent!")
        
    form = ContactForm()
    return render(request, "realty/contact.html", {'logo': logo, 'ticont': ticont, 'call_us': call_us, 'email_us': email_us, 'social_us': social_us, 'cont_form': cont_form, 'form': form})


def register_request(request):
    logo = Logo.objects.order_by()[:1]
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="realty/register.html", context={"register_form": form, 'logo': logo})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {username}. ")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="realty/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def create_project(request):

    if request.method == "POST":
        form = ProductForm(request.POST)
        imageform = ImageForm(request.POST)
        files = request.FILES.getlist("image")
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            for i in files:
                Image.objects.create(product=f, image=i)
            messages.success(request, "New Project Added")
            return HttpResponseRedirect("/objects")
        else:
            print(form.errors)
    else:
        form = ProductForm()
        imageform = ImageForm()

    return render(request, "realty/create.html", {"form": form, "imageform": imageform})


#  for i in files:
    # print(i)
    # Image.objects.create(image=i)

class RealtyViews(DetailView):
    model = Product
    template_name = 'realty/realty_view.html'
    context_object_name = 'realty'

class RealtyUpdate(UpdateView):
    model = Product
    template_name = 'realty/create.html'
    form_class = ProductForm #nathing else mater form
        
    def get(self, request, **kwargs):
        if self.get_object().author == self.request.user:
            return UpdateView.get(self, request, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, "You can only change your own entries")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RealtyDelete(DeleteView):
    model = Product
    success_url = '/objects'
    template_name = 'realty/views-delete.html'

    def get(self, request, **kwargs):
        if self.get_object().author == self.request.user:
            return DeleteView.get(self, request, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, "You can only delete your own entries")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


   
def news(request):
    news = News_articl.objects.all()
    some_news = News_articl.objects.order_by()[:3]
    latest_news = News_articl.objects.order_by()[:1]

    return render(request, "realty/news.html", {"news": news, "some_news": some_news, "latest_news": latest_news})    