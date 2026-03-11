from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('note/', views.note, name='note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    
    # La virgule à la fin de la ligne du dessus est importante !
    path('update_note/<str:pk>/', views.update_note, name='update_note'),

    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]