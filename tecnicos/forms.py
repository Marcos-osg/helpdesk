from django.forms import ModelForm
from tecnicos.models import Tecnico

class TecnicoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Tecnico