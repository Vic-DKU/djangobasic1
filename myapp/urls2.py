#myapp - urls

from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pet_list, name='pet_list'),
]

