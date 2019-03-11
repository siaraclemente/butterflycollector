from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'), 
   path('butterflies/', views.butterflies_index, name='index'),
   path('butterflies/<int:butterfly_id>/', views.butterflies_detail, name='detail'),
]