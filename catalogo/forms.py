from django import forms
from .models import MensagemContato


class MensagemContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'telefone', 'email', 'interesse', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'WhatsApp'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'interesse': forms.TextInput(attrs={'placeholder': 'Qual reboque você procura?'}),
            'mensagem': forms.Textarea(attrs={'placeholder': 'Conte um pouco do que você precisa', 'rows': 4}),
        }
