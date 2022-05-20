from django.urls import path
from . import views as learning_views

urlpatterns = [
    path('', learning_views.home, name="learning_home"),    
    path('A1', learning_views.A1, name="learning_A1"),        
    path('A1/videos', learning_views.A1videos, name="learning_A1videos"),        
]


