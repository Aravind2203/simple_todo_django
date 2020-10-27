from django.contrib import admin

# Register your models here.
from .models import Todolist

admin.site.register(Todolist)