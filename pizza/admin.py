from django.contrib import admin
from .models import Pizza



@admin.register(Pizza)
class PizzaAdmin (admin.ModelAdmin):
    list_display = ['nazwa', 'cena']
    list_filter = ['nazwa']