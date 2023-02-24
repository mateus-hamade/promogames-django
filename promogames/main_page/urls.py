from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('script/', views.script, name='script'),
    path('profile/', views.profile, name='profile')
]
