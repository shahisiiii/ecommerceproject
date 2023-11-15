from django.contrib import admin
from ecommapp.models import Categories
from ecommapp.models import Products

# Register your models here.

admin.site.register(Categories)
admin.site.register(Products)