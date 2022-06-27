from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'plantillas_log/registro.html'
  success_url = reverse_lazy('login')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class LogappProfile(DetailView):

    model = User
    template_name = "plantillas_log/detalles.html"


class LogappUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "plantillas_log/usuario.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("logapp_profile", kwargs={"pk": self.request.user.id})


