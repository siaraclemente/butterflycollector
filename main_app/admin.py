from django.contrib import admin
from .models import Butterfly, Feeding, Flower, Photo

# Register your models here.
admin.site.register(Butterfly)
admin.site.register(Feeding)
admin.site.register(Flower)
admin.site.register(Photo)

