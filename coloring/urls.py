from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('home', views.home, name='home'),
    path('pages', views.pages, name='pages'),
    path('npages', views.npages, name='npages'),

]
