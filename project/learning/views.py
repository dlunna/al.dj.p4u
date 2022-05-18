from django.shortcuts import render, get_object_or_404

# Create your views here.

def home (request):    
    return render(request, "learning/nivelA1.html")

#se recupera 1 de acuerdo al ID
def A1(request):
    return render(request, 'learning/nivelA1.html')

def A1videos(request):
    return render(request, 'learning/nivelA1videos.html')
