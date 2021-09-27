from django.forms import ModelForm
from tecnicos.models import Tecnico
from django import forms

class TecnicoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Tecnico

        widgets = {
            'ativo':forms.RadioSelect(),
        }