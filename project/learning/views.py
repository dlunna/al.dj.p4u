from django.shortcuts import render, get_object_or_404

# Create your views here.

def home (request):    
    return render(request, "learning/nivelA1.html")

#se recupera 1 de acuerdo al ID
def A1(request):
    return render(request, 'learning/nivelA1.html')

def A1SBvideos(request):
    return render(request, 'learning/nivelA1SBvideos.html')

def A1SBaudios(request):
    return render(request, 'learning/nivelA1SBaudios.html')

def A1SBscripts(request):
    return render(request, 'learning/nivelA1SBscripts.html')
