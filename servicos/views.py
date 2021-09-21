from django.contrib import messages
from django.shortcuts import redirect, render
from servicos.forms import ServicoForm
from servicos.models import Servico

# Create your views here.
def service(request):
    context = {'servicos':Servico.objects.all()}
    return render(request, 'servicos/servicos.html',context)

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

def detail_service(request, id_servico):
    servico = {'servico':Servico.objects.get(id=id_servico)}
    return render(request, 'servicos/servico_detalhe.html',servico)
