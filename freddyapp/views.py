from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Animatronic, Party
from .forms import AnimatronicForm, RegisterForm


class AnimatronicList(ListView):
    model = Animatronic
    template_name = 'freddyapp/list.html'
    context_object_name = 'animatronics'


class AnimatronicDetail(LoginRequiredMixin, DetailView):
    model = Animatronic
    template_name = 'freddyapp/view.html'
    pk_url_kwarg = 'id'
    context_object_name = 'animatronic'


class AnimatronicCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Animatronic
    form_class = AnimatronicForm
    template_name = 'freddyapp/new.html'
    permission_required = 'freddyapp.add_animatronic'
    success_url = reverse_lazy('animatronic_list')


class AnimatronicUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Animatronic
    form_class = AnimatronicForm
    template_name = 'freddyapp/edit.html'
    permission_required = 'freddyapp.change_animatronic'
    success_url = reverse_lazy('animatronic_list')
    pk_url_kwarg = 'id'


class AnimatronicDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Animatronic
    template_name = 'freddyapp/delete.html'
    permission_required = 'freddyapp.delete_animatronic'
    success_url = reverse_lazy('animatronic_list')
    pk_url_kwarg = 'id'
    context_object_name = 'animatronic'


def newuser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Agregar usuario al grupo Client
            client_group = Group.objects.get(name='Client')
            user.groups.add(client_group)
            login(request, user)
            return redirect('animatronic_list')
    else:
        form = RegisterForm()
    
    return render(request, 'freddyapp/register.html', {'form': form})


def theme(request):
    response = redirect('animatronic_list')
    response.set_cookie('theme', 'dark')
    return response


def clearcookies(request):
    response = redirect('animatronic_list')
    response.delete_cookie('theme')
    return response

