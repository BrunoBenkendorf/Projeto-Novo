from django import forms
from .models import Peca,Cliente, Funcionario
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
class LoginClienteForm(forms.Form):
    email = forms.EmailField(
        label="Email do Cliente",
        widget=forms.EmailInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            'placeholder': 'exemplo@email.com'
        })
    )
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            'placeholder': 'Digite sua senha'
        })
    )

class LoginFuncionarioForm(forms.Form):
    email = forms.EmailField(
        label="Email do Funcionário",
        widget=forms.EmailInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            'placeholder': 'seuemail@empresa.com'
        })
    )
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            'placeholder': 'Digite sua senha'
        })
    )
class CadastroClienteForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            'placeholder': 'Digite sua senha'
        })
    )

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cep', 'rua', 'bairro', 'cidade', 'estado', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'exemplo@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': '(00) 00000-0000'
            }),
            'cep': forms.TextInput(attrs={
                'id': 'cep',
                'maxlength': '9',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': '00000-000'
            }),
            'rua': forms.TextInput(attrs={
                'id': 'rua',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            }),
            'bairro': forms.TextInput(attrs={
                'id': 'bairro',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            }),
            'cidade': forms.TextInput(attrs={
                'id': 'cidade',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            }),
            'estado': forms.TextInput(attrs={
                'id': 'estado',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            }),
        }
class CadastroFuncionarioForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
            'placeholder': 'Digite sua senha'
        })
    )

    class Meta:
        model = Funcionario
        fields = ['nome', 'email', 'cargo', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'email@empresa.com'
            }),
            'cargo': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Cargo ou função'
            }),
        }