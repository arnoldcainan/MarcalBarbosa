from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Sistema de Login/Logout nativo do Django
    # Isso habilita rotas como: /accounts/login/ e /accounts/logout/
    path('accounts/', include('django.contrib.auth.urls')),

    # Rotas do Core (Página inicial pública)
    path('', include('core.urls')),

    # Rotas da Agenda (Dashboard e Contatos)
    path('agenda/', include('agenda.urls')),
]