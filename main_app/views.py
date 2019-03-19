from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Butterfly, Flower, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'butterflycollector'

# Create your views here.
class ButterflyCreate(LoginRequiredMixin, CreateView):
  model = Butterfly
  fields = ['name', 'type', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ButterflyUpdate(LoginRequiredMixin, UpdateView):
  model = Butterfly
  fields = ['type', 'description', 'age']

class ButterflyDelete(LoginRequiredMixin, DeleteView):
  model = Butterfly
  success_url = '/butterflies/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def butterflies_index(request):
    butterflies = Butterfly.objects.filter(user=request.user)
    return render(request, 'butterflies/index.html', { 'butterflies': butterflies })

@login_required
def butterflies_detail(request, butterfly_id):
  butterfly = Butterfly.objects.get(id=butterfly_id)
  flowers_butterfly_doesnt_have = Flower.objects.exclude(id__in = butterfly.flowers.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'butterflies/detail.html', { 
    'butterfly': butterfly, 'feeding_form': feeding_form,
    'flowers': flowers_butterfly_doesnt_have
  })

@login_required
def add_feeding(request, butterfly_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.butterfly_id = butterfly_id
    new_feeding.save()
  return redirect('detail', butterfly_id=butterfly_id)

@login_required
def add_photo(request, butterfly_id):
	# photo-file was the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to butterfly_id or butterfly (if you have a butterfly object)
      photo = Photo(url=url, butterfly_id=butterfly_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', butterfly_id=butterfly_id)

@login_required
def assoc_flower(request, butterfly_id, flower_id):
  Butterfly.objects.get(id=butterfly_id).flowers.add(flower_id)
  return redirect('detail', butterfly_id=butterfly_id)

@login_required
def unassoc_flower(request, butterfly_id, flower_id):
  Butterfly.objects.get(id=butterfly_id).flowers.remove(flower_id)
  return redirect('detail', butterfly_id=butterfly_id)

class FlowerList(LoginRequiredMixin, ListView):
  model = Flower

class FlowerDetail(LoginRequiredMixin, DetailView):
  model = Flower

class FlowerCreate(LoginRequiredMixin, CreateView):
  model = Flower
  fields = '__all__'

class FlowerUpdate(LoginRequiredMixin, UpdateView):
  model = Flower
  fields = ['name', 'color']

class FlowerDelete(LoginRequiredMixin, DeleteView):
  model = Flower
  success_url = '/flowers/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

  


