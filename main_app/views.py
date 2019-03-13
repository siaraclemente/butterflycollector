from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Butterfly, Flower
from .forms import FeedingForm

# Create your views here.
class ButterflyCreate(CreateView):
  model = Butterfly
  fields = '__all__'

class ButterflyUpdate(UpdateView):
  model = Butterfly
  fields = ['type', 'description', 'age']

class ButterflyDelete(DeleteView):
  model = Butterfly
  success_url = '/butterflies/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def butterflies_index(request):
    butterflies = Butterfly.objects.all()
    return render(request, 'butterflies/index.html', { 'butterflies': butterflies })

def butterflies_detail(request, butterfly_id):
  butterfly = Butterfly.objects.get(id=butterfly_id)
  flowers_butterfly_doesnt_have = Flower.objects.exclude(id__in = butterfly.flowers.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'butterflies/detail.html', { 
    'butterfly': butterfly, 'feeding_form': feeding_form,
    'flowers': flowers_butterfly_doesnt_have
  })

def add_feeding(request, butterfly_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.butterfly_id = butterfly_id
    new_feeding.save()
  return redirect('detail', butterfly_id=butterfly_id)

def assoc_flower(request, butterfly_id, flower_id):
  Butterfly.objects.get(id=butterfly_id).flowers.add(flower_id)
  return redirect('detail', butterfly_id=butterfly_id)

def unassoc_flower(request, butterfly_id, flower_id):
  Butterfly.objects.get(id=butterfly_id).flowers.remove(flower_id)
  return redirect('detail', butterfly_id=butterfly_id)

class FlowerList(ListView):
  model = Flower

class FlowerDetail(DetailView):
  model = Flower

class FlowerCreate(CreateView):
  model = Flower
  fields = '__all__'

class FlowerUpdate(UpdateView):
  model = Flower
  fields = ['name', 'color']

class FlowerDelete(DeleteView):
  model = Flower
  success_url = '/flowers/'  


