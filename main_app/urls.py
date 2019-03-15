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
   path('butterflies/<int:butterfly_id>/add_feeding/', views.add_feeding, name='add_feeding'),
   path('butterflies/<int:butterfly_id>/add_photo/', views.add_photo, name='add_photo'),
   path('butterflies/<int:butterfly_id>/assoc_flower/<int:flower_id>/', views.assoc_flower, name='assoc_flower'),
   path('butterflies/<int:butterfly_id>/unassoc_flower/<int:flower_id>/', views.unassoc_flower, name='unassoc_flower'),
   path('flowers/', views.FlowerList.as_view(), name='flowers_index'),
   path('flowers/<int:pk>/', views.FlowerDetail.as_view(), name='flowers_detail'),
   path('flowers/create/', views.FlowerCreate.as_view(), name='flowers_create'),
   path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flowers_update'),
   path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flowers_delete'),
   
]