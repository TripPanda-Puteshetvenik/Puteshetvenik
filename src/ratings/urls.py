from django.urls import path
from . import views
urlpatterns = [
    path('add/<int:post_pk>/', views.add_rating, name='add_rating'),
]
