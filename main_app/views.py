from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Butterfly

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def butterflies_index(request):
    butterflies = Butterfly.objects.all()
    return render(request, 'butterflies/index.html', { 'butterflies': butterflies })

def butterflies_detail(request, butterfly_id):
  butterfly = Butterfly.objects.get(id=butterfly_id)
  return render(request, 'butterflies/detail.html', { 'butterfly': butterfly })

class ButterflyCreate(CreateView):
  model = Butterfly
  fields = '__all__'
  success_url = '/butterflies/'

class ButterflyUpdate(UpdateView):
  model = Butterfly
  fields = ['type', 'description', 'age']

class ButterflyDelete(DeleteView):
  model = Butterfly
  success_url = '/butterflies/'
