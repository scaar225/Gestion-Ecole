from django.contrib import admin
from django.urls import path
from inscription.views import acceuil , liste , ajout
urlpatterns = [
    path('', acceuil, name='home'), 
    path('liste',liste,name='list'),
    path('ajout',ajout,name='add'),


]
