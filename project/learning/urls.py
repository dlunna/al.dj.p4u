from django.urls import path
from . import views as learning_views

urlpatterns = [
    path('', learning_views.home, name="learning_home"),    
    path('A1', learning_views.A1, name="learning_A1"),        
    path('A1/SB/videos', learning_views.A1SBvideos, name="learning_A1SBvideos"),        
    path('A1/SB/audios', learning_views.A1SBaudios, name="learning_A1SBaudios"),        
    path('A1/SB/scripts', learning_views.A1SBscripts, name="learning_A1SBscripts"),        
]


