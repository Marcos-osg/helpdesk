from django import forms
from produtos.models import Produto
from django.forms import ModelForm
from django import forms

class ProdutoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Produto

        widgets = {
            'disponivel':forms.RadioSelect(),
        }