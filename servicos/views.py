from django.contrib import messages
from django.shortcuts import redirect, render
from servicos.forms import ServicoForm
from servicos.models import Servico
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def service(request):
    context = {'servicos':Servico.objects.all()}
    return render(request, 'servicos/servicos.html',context)

@login_required(login_url='login')
def new_service(request):
    if request.method != 'POST':
        form = ServicoForm
        context = {'form':form}
        return render(request, 'servicos/servico_form.html', context)
    form = ServicoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Serviço adicionado com sucesso!')
        return redirect('services')

    context = {'form':form}
    return render(request,'servicos/servico_form.html', context)

@login_required(login_url='login')
def detail_service(request, id=None):
    servico = {'servico':Servico.objects.get(id=id)}
    return render(request, 'servicos/servico_detalhe.html',servico)
