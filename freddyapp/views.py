from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from .models import Animatronic, Party
from .forms import AnimatronicForm, PartyFormSet, RegisterForm


# Vista para listar todos los animatronicos
def animatronic_list(request):
    # Obtener todos los animatronicos de la base de datos
    animatronics = Animatronic.objects.all()
    return render(request, 'freddyapp/list.html', {'animatronics': animatronics})


# Vista para crear un nuevo animatronico
@login_required
@permission_required('freddyapp.add_animatronic', raise_exception=True)
def animatronic_new(request):
    if request.method == 'POST':
        # Si el formulario se envio
        form = AnimatronicForm(request.POST)
        formset = PartyFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            # Guardar el animatronico
            animatronic = form.save()
            
            # Guardar las fiestas
            formset.instance = animatronic
            formset.save()
            
            # Redirigir a la lista
            return redirect('animatronic_list')
    else:
        # Mostrar formulario vacio
        form = AnimatronicForm()
        formset = PartyFormSet()
    
    return render(request, 'freddyapp/new.html', {
        'form': form,
        'formset': formset
    })


# Vista para ver los detalles de un animatronico
@login_required
def animatronic_view(request, id):
    # Obtener el animatronico
    animatronic = get_object_or_404(Animatronic, pk=id)
    return render(request, 'freddyapp/view.html', {'animatronic': animatronic})


# Vista clase para editar un animatronico
class AnimatronicUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Animatronic
    form_class = AnimatronicForm
    template_name = 'freddyapp/edit.html'
    permission_required = 'freddyapp.change_animatronic'
    success_url = reverse_lazy('animatronic_list')
    pk_url_kwarg = 'id'


# Vista clase para eliminar un animatronico
class AnimatronicDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Animatronic
    template_name = 'freddyapp/delete.html'
    permission_required = 'freddyapp.delete_animatronic'
    success_url = reverse_lazy('animatronic_list')
    pk_url_kwarg = 'id'


# Vista para registrar un nuevo usuario
def newuser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = form.save()
            
            # Agregar el usuario al grupo Client
            client_group = Group.objects.get(name='Client')
            user.groups.add(client_group)
            
            # Iniciar sesion automaticamente
            login(request, user)
            
            # Redirigir a la lista
            return redirect('animatronic_list')
    else:
        form = RegisterForm()
    
    return render(request, 'freddyapp/register.html', {'form': form})


# Vista para guardar la cookie del tema oscuro
def theme(request):
    response = redirect('animatronic_list')
    response.set_cookie('theme', 'dark')
    return response


# Vista para borrar la cookie del tema
def clearcookies(request):
    response = redirect('animatronic_list')
    response.delete_cookie('theme')
    return response


# Vista para cerrar sesion
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('animatronic_list')
