from datetime import date
from typing import Text

from django.forms.widgets import DateTimeInput
from django.utils.formats import date_format
from servicos.models import Servico
from django.forms import ModelForm
from django import forms

class ServicoForm(ModelForm):
    class Meta:
        fields ='__all__'
        model = Servico

        widgets ={
            'tipo_servico':forms.RadioSelect(),
            'status':forms.RadioSelect(),
        }