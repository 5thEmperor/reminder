from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_reminder, name='create_reminder'),
    # Add more URL patterns as needed
]
