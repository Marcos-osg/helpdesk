from django.contrib import auth,messages
from django.shortcuts import redirect, render
from accounts import forms
from accounts.models import Cliente, User
from accounts.forms import ClienteForm
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required

# contas e usuarios
@login_required(login_url='login')
def cadastrar(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro_form.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not email or not usuario or not senha or not senha2:
        messages.error(request,'Nenhum campo pode estar vazio')
        return render(request, 'accounts/cadastro_form.html')
    try:
        validate_email(email)
    except:
        messages.error(request,'Email invalido')
        return render(request, 'accounts/cadastro_form.html')
    if senha != senha2:
        messages.error(request,'Senhas não conferem')
        return render(request, 'accounts/cadastro_form.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request,'Usuario já existente')
        return render(request, 'accounts/cadastro_form.html')
    if User.objects.filter(email=email).exists():
        messages.error(request,'Email já existente')
        return render(request, 'accounts/cadastro_form.html')
    messages.success(request,'Sucesso ao cadastrar, Efetue o login')

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()

    return redirect('login')


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request,'Usuario ou senha invalidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('login-sucess')
        
@login_required(login_url='login')
def login_sucess(request):
    return render(request, 'accounts/login_sucess.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

# clientes
@login_required(login_url='login')
def novo_cliente(request):
    if request.method != 'POST':
        cliente = ClienteForm
        context = {'form':cliente}
        return render(request, 'clientes/cliente_form.html',context)
    form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Cliente Adicionado com sucesso!')
        return redirect('client-list')
    context = {'form': form}
    return render(request,'clientes/cliente_form.html', context)

@login_required(login_url='login')
def clientes(request):
    cliente = {'clientes':Cliente.objects.all()}
    return render(request, 'clientes/clientes.html', cliente)

@login_required(login_url='login')
def detalhe_cliente(request, id=None):
    cliente = {'cliente':Cliente.objects.get(pk=id)}
    return render(request, 'clientes/cliente_detalhe.html', cliente)

@login_required(login_url='login')
def excluir_cliente(request, id=None):
    cliente = Cliente.objects.get(pk=id)
    if request.method != 'POST':
        context = {'cliente':cliente}
        return render(request, 'clientes/cliente_delete.html', context)
    cliente.delete()
    return redirect('client-list')