from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea
from .forms import TareaForm


def index(request):
    if request.user.is_authenticated:
        return redirect('lista_tareas')
    return render(request, 'index.html')


class ListaTareasView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'lista.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user).order_by('-creada')


class DetalleTareaView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'detalle.html'
    success_url = reverse_lazy('lista_tareas')

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)


class AgregarTareaView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'agregar.html'
    success_url = reverse_lazy('lista_tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class EliminarTareaView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'eliminar.html'
    success_url = reverse_lazy('lista_tareas')

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'La tarea ha sido eliminada correctamente.')
        return super().delete(request, *args, **kwargs)


class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registro.html'
    success_url = reverse_lazy('lista_tareas')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lista_tareas')


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')