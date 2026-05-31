from django.contrib import admin
from .models import Continent, Country, TravelType

@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'continent', 'flag']
    list_filter = ['continent']

@admin.register(TravelType)
class TravelTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
