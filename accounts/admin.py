from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from accounts.forms import UserChangeForm,UserCreationForm
from accounts.models import Cliente, User

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo','cpf','telefone','endereco','cidade')