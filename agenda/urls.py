from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # CRUD Contatos
    path('contatos/', views.ContatoListView.as_view(), name='lista_contatos'),
    path('contatos/novo/', views.ContatoCreateView.as_view(), name='criar_contato'),
    path('contatos/<int:pk>/editar/', views.ContatoUpdateView.as_view(), name='editar_contato'),
    path('contatos/<int:pk>/deletar/', views.ContatoDeleteView.as_view(), name='deletar_contato'),
    path('etiquetas/gerar/', views.gerar_etiquetas, name='gerar_etiquetas'),

]