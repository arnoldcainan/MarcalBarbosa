from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login


# View de Cadastro
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redireciona para login após criar
    template_name = 'registration/signup.html'

    def form_valid(self, form):

        user = form.save()
        login(self.request, user)
        return redirect('dashboard')
        return super().form_valid(form)


# Mantendo a index que já existia...
def index(request):
    return render(request, 'core/index.html')