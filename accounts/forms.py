from django.contrib.auth import forms
from accounts.models import User, Cliente
from django.forms import ModelForm


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class ClienteForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Cliente