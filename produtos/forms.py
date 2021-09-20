from produtos.models import Produto
from django.forms import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Produto