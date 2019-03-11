from django.shortcuts import render
from django.http import HttpResponse

class Butterfly:
    def __init__(self, name, type, description, age):
        self.name = name
        self.type = type
        self.description = description
        self.age = age

butterflies = [
    Butterfly('Milbert', 'milbert’s tortoiseshell', 'outgoing little bugger', 3),
    Butterfly('Lily', 'monarch', 'loves lillies', 0),
    Butterfly('Blue', 'karner blue', 'old man', 4)
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Yerrrrr</h1>')

def about(request):
    return render(request, 'about.html')

def butterflies_index(request):
    return render(request, 'butterflies/index.html', { 'butterflies': butterflies })
