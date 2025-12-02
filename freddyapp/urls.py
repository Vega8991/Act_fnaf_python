from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('list', views.AnimatronicList.as_view(), name='animatronic_list'),
    path('new', views.AnimatronicCreate.as_view(), name='animatronic_new'),
    path('<int:id>/view', views.AnimatronicDetail.as_view(), name='animatronic_view'),
    path('<int:id>/edit', views.AnimatronicUpdate.as_view(), name='animatronic_edit'),
    path('<int:id>/delete', views.AnimatronicDelete.as_view(), name='animatronic_delete'),
    path('newuser', views.newuser, name='newuser'),
    path('login', LoginView.as_view(template_name='freddyapp/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='/freddyapp/list'), name='logout'),
    path('theme', views.theme, name='theme'),
    path('clearcookies', views.clearcookies, name='clearcookies'),
]
