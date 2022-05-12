from django.shortcuts import render, get_object_or_404

# Create your views here.

def home (request):    
    return render(request, "learning/nivel.html")

#se recupera 1 de acuerdo al ID
def page(request, page_id, page_slug):
    objeto = page_id
    return render(request, 'learning/nivel.html', {'llave':objeto})
