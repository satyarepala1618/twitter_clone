from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
]
