from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')

def myemail(request):
    return HttpResponse("<p>dlunna@gmail.com</p>")

