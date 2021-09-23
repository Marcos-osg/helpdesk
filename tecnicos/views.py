from uuid import uuid4
from django.contrib import messages
from tecnicos.models import Tecnico
from django.shortcuts import redirect, render
from tecnicos.forms import TecnicoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def tecnico(request):
    context = {'tecnicos':Tecnico.objects.all()}
    return render(request, 'tecnicos/tecnico.html',context)

@login_required(login_url='login')
def new_technician(request):
    if request.method != 'POST':
        form = TecnicoForm
        context = {'form':form}
        return render(request, 'tecnicos/tecnico_form.html', context)
    form = TecnicoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Tecnico Adicionado com sucesso!')
        return redirect('technician')

    context = {'form':form}
    return render(request, 'tecnicos/tecnico_form.html', context)

@login_required(login_url='login')
def detail_technician(request, id=None):
    tecnico = {'tecnico':Tecnico.objects.get(pk=id)}
    return render(request, 'tecnicos/tecnico_detalhes.html',tecnico) 

@login_required(login_url='login')
def delete_technician(request, id=None):
    tecnico = Tecnico.objects.get(pk=id)
    if request.method != 'POST':
        context = {'tecnico': tecnico}
        return render(request, 'tecnicos/deletar_tecnico.html', context)
    tecnico.delete()
    return redirect('technician')

@login_required(login_url='login')
def edita_tecnico(request, id=None):
    produto = Tecnico.objects.get(pk=id)
    formset = TecnicoForm(instance=produto)

    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('technician')
    context = {'tecnico':formset}
    return render(request, 'tecnicos/tecnico_edit.html', context)