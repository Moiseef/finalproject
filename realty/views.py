from django.shortcuts import render
 
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def realty(request):
    return render(request, "realty.html")    
def contact(request):
    return render(request, "contact.html")        