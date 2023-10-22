from django.urls import path
from . import views

urlpatterns = [
    path('decode/', views.decode, name='decode'),
    path('', views.index, name='index'),

]
