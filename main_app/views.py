from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Butterfly
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'butterflies/detail.html', { 
    'butterfly': butterfly, 'feeding_form': feeding_form
    })

def add_feeding(request, butterfly_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.butterfly_id = butterfly_id
    new_feeding.save()
  return redirect('detail', butterfly_id=butterfly_id)

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
