from django.contrib import messages
from tecnicos.models import Tecnico
from django.shortcuts import redirect, render
from tecnicos.forms import TecnicoForm

# Create your views here.
def tecnico(request):
    context = {'tecnicos':Tecnico.objects.all()}
    return render(request, 'tecnicos/tecnico.html',context)


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


def detail_technician(request, id_tecnico):
    tecnico = {'tecnico':Tecnico.objects.get(pk=id_tecnico)}
    return render(request, 'tecnicos/tecnico_detalhes.html',tecnico)