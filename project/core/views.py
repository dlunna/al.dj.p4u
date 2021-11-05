from django.shortcuts import render, HttpResponse

from django.conf import settings
from django.utils import translation

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def message(request):
    return render(request, 'core/message.html')

def whatisele(request):
    return render(request, 'core/whatisele.html')

def components(request):
    return render(request, 'core/components.html')

def methodology(request):
    return render(request, 'core/methodology.html')

def contact(request):
    return render(request, 'core/contact.html')

#

#def simple(request):
#    return render(request, 'core/simple.html')

def myemail(request):
    return HttpResponse("<p>dlunna@gmail.com</p>")

def simple(request):
    return render(request, 'core/simple.html')

