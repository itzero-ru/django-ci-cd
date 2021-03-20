from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # index без скобок (), т.к. нам не нужновыполнение, а нужно просто обратится
    path('about', views.about, name='about'),
]