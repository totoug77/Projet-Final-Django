from django.urls import path
from . import views

urlpatterns = [
    path('note/', views.note, name='note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('', views.home, name='home'), ]

from . import views

urlpatterns = [
    # ... tes autres urls ...
    path('update_note/<str:pk>/', views.update_note, name="update_note"),
]