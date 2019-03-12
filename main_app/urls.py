from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'), 
   path('butterflies/', views.butterflies_index, name='index'),
   path('butterflies/<int:butterfly_id>/', views.butterflies_detail, name='detail'),
   path('butterflies/create/', views.ButterflyCreate.as_view(), name='butterflies_create'),
   path('butterflies/<int:pk>/update/', views.ButterflyUpdate.as_view(), name='butterflies_update'),
   path('butterflies/<int:pk>/delete/', views.ButterflyDelete.as_view(), name='butterflies_delete'),
]