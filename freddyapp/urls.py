from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

# URLs de la aplicacion
urlpatterns = [
    # Lista de animatronicos
    path('list', views.animatronic_list, name='animatronic_list'),
    
    # Crear nuevo animatronico
    path('new', views.animatronic_new, name='animatronic_new'),
    
    # Ver detalle de animatronico
    path('<int:id>/view', views.animatronic_view, name='animatronic_view'),
    
    # Editar animatronico
    path('<int:id>/edit', views.AnimatronicUpdate.as_view(), name='animatronic_edit'),
    
    # Eliminar animatronico
    path('<int:id>/delete', views.AnimatronicDelete.as_view(), name='animatronic_delete'),
    
    # Registro de usuario
    path('newuser', views.newuser, name='newuser'),
    
    # Login
    path('login', LoginView.as_view(template_name='freddyapp/login.html'), name='login'),
    
    # Logout
    path('logout', views.logout_view, name='logout'),
    
    # Tema oscuro
    path('theme', views.theme, name='theme'),
    
    # Borrar cookies
    path('clearcookies', views.clearcookies, name='clearcookies'),
]
