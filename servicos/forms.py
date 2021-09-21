from servicos.models import Servico
from django.forms import ModelForm

class ServicoForm(ModelForm):
    class Meta:
        fields ='__all__'
        model = Servico