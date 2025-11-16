from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea

class UsuarioTareaMixin(LoginRequiredMixin):
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)