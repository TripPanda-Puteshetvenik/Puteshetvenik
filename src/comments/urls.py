from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:post_pk>/', views.add_comment, name='add_comment'),
    path('delete/<int:pk>/', views.delete_comment, name='delete_comment'),
]
