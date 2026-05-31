from django.urls import path
from . import views

urlpatterns = [
    path('continent/<slug:slug>/', views.continent_posts, name='continent_posts'),
    path('country/<slug:slug>/', views.country_posts, name='country_posts'),
    path('type/<str:name>/', views.travel_type_posts, name='travel_type_posts'),
]
