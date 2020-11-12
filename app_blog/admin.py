#Zainporotowanie admin i modelu Post

from django.contrib import admin
from .models import Post

#Rejestrujemy model Post w admin

admin.site.register(Post)
