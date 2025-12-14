from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import date, timedelta
from .models import Contato
from .forms import ContatoForm


# Dashboard: Aniversariantes e Resumo
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'core/index.html')  # Landing page pública

    # Lógica de Aniversariantes da Semana
    hoje = date.today()
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timedelta(days=6)

    contatos = Contato.objects.filter(usuario=request.user)
    aniversariantes = []

    # Filtragem Python (mais simples para lidar com virada de ano e dia/mês separado)
    for c in contatos:
        if c.data_nascimento:
            niver_este_ano = c.data_nascimento.replace(year=hoje.year)
            if inicio_semana <= niver_este_ano <= fim_semana:
                aniversariantes.append(c)

    context = {
        'total_contatos': contatos.count(),
        'aniversariantes': aniversariantes
    }
    return render(request, 'agenda/dashboard.html', context)


# CRUD Padrão
class ContatoListView(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'agenda/lista_contatos.html'

    def get_queryset(self):
        qs = Contato.objects.filter(usuario=self.request.user)

        # 1. Busca Rápida (Genérica)
        termo = self.request.GET.get('q')
        if termo:
            qs = qs.filter(
                Q(nome__icontains=termo) |
                Q(email__icontains=termo) |
                Q(cidade__icontains=termo)
            )

        # 2. Filtros Avançados (Específicos)
        filtro_bairro = self.request.GET.get('filtro_bairro')
        filtro_cidade = self.request.GET.get('filtro_cidade')
        filtro_estado = self.request.GET.get('filtro_estado')

        if filtro_bairro:
            qs = qs.filter(bairro__icontains=filtro_bairro)

        if filtro_cidade:
            qs = qs.filter(cidade__icontains=filtro_cidade)

        if filtro_estado:
            qs = qs.filter(estado__iexact=filtro_estado)  # Estado é exato (ex: SP)

        return qs

class ContatoCreateView(LoginRequiredMixin, CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'agenda/form_contato.html'
    success_url = reverse_lazy('lista_contatos')

    def form_valid(self, form):
        # O dono do contato é forçado a ser o usuário logado
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ContatoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'agenda/form_contato.html'
    success_url = reverse_lazy('lista_contatos')

    def get_queryset(self):
        return Contato.objects.filter(usuario=self.request.user)


class ContatoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contato
    template_name = 'agenda/confirmar_delete.html'
    success_url = reverse_lazy('lista_contatos')

    def get_queryset(self):
        return Contato.objects.filter(usuario=self.request.user)


def gerar_etiquetas(request):
    if request.method == 'POST':
        # Pega os IDs selecionados no formulário da lista
        ids_selecionados = request.POST.getlist('selection')

        # Filtra apenas os contatos que pertencem ao usuário E que foram selecionados
        contatos = Contato.objects.filter(
            usuario=request.user,
            id__in=ids_selecionados
        )

        return render(request, 'agenda/etiquetas.html', {'contatos': contatos})

    # Se tentar acessar via GET sem selecionar nada, redireciona
    return redirect('lista_contatos')