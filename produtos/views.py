from django.shortcuts import redirect, render
from produtos.forms import ProdutoForm
from produtos.models import Produto
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def new_product(request):
    if request.method != 'POST':
        form = ProdutoForm
        context ={'form':form}
        return render(request, 'produtos/produto_form.html', context)
    form = ProdutoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Produto adicionado com sucesso!')
        return redirect('product')

    context = {'form':form}
    return render(request, 'produtos/produto_form.html',context)

@login_required(login_url='login')
def produto(request):
    context = {'produtos':Produto.objects.all()}
    return render(request, 'produtos/produtos.html',context)

@login_required(login_url='login')
def produto_detalhe(request, id=None):
    produto = {'produto':Produto.objects.get(pk=id)}
    return render(request, 'produtos/produto_detalhe.html', produto)

@login_required(login_url='login')
def edita_produto(request, id=None):
    produto = Produto.objects.get(pk=id)
    formset = ProdutoForm(instance=produto)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('product')
    context = {'produto':formset}
    return render(request, 'produtos/produto_edit.html', context)

    
@login_required(login_url='login')
def deletar_produto(request, id=None):
    produto = Produto.objects.get(pk=id) 
    if request.method == 'POST':
        produto.delete()
        return redirect('product')
    return render(request,'produtos/deletar_produto.html',{'produto':produto})