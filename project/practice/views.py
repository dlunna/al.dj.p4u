from django.shortcuts import render, HttpResponse

# Create your views here.

def LevelA1(request):
    return render(request, 'practice/LevelA1.html')
