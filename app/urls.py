from django.urls import path
from . import views

urlpatterns = [
    path('note/', views.note, name='note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('', views.home, name='home'),
]