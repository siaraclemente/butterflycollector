from django.contrib import admin
from .models import Butterfly, Feeding, Flower

# Register your models here.
admin.site.register(Butterfly)
admin.site.register(Feeding)
admin.site.register(Flower)

