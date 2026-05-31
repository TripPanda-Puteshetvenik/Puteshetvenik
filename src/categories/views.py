from django.shortcuts import render, get_object_or_404
from .models import Continent, Country, TravelType
from posts.models import Post


def continent_posts(request, slug):
    continent = get_object_or_404(Continent, slug=slug)
    posts = Post.objects.filter(country__continent=continent, published=True).order_by('-created_at')
    return render(request, 'categories/continent.html', {'continent': continent, 'posts': posts})


def country_posts(request, slug):
    country = get_object_or_404(Country, slug=slug)
    posts = Post.objects.filter(country=country, published=True).order_by('-created_at')
    return render(request, 'categories/country.html', {'country': country, 'posts': posts})


def travel_type_posts(request, name):
    travel_type = get_object_or_404(TravelType, name=name)
    posts = Post.objects.filter(travel_types=travel_type, published=True).order_by('-created_at')
    return render(request, 'categories/travel_type.html', {'travel_type': travel_type, 'posts': posts})
