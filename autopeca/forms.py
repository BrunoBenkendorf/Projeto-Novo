from django import forms
from .models import Peca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome', 'descricao', 'preco', 'estoque', 'categoria', 'fabricante', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Ex: Filtro de Óleo'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'rows': 4,
                'placeholder': 'Descreva a peça aqui...'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'R$ 99.90'
            }),
            'estoque': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Quantidade disponível'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
            }),
            'fabricante': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 bg-white cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-red-800 file:text-white hover:file:bg-red-700'
            }),
        }
