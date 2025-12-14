from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ['usuario', 'criado_em']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            # O JavaScript é acionado aqui no onblur
            'cep': forms.TextInput(attrs={'onblur': 'buscarCep(this.value)', 'placeholder': '00000-000'}),
        }