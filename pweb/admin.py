from django.contrib import admin
from .models import Client, Contact, Image

# Register your models here.

admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Image)

