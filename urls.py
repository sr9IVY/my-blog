

from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='home'),  # Maps root URL to the home view
]
