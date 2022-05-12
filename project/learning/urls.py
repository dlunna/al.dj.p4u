from django.urls import path
from . import views as learning_views

urlpatterns = [
    path('', learning_views.home, name="learning_levelA1"),    
    path('<int:page_id>/<slug:page_slug>/', learning_views.page, name="page"),
]


