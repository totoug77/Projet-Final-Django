from django.contrib import admin
from .models import Todolist, Categorie, Produit

admin.site.register(Todolist)
admin.site.register(Categorie)
admin.site.register(Produit)