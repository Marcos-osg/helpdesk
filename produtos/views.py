from django.shortcuts import redirect, render
from produtos.forms import ProdutoForm
from produtos.models import Produto
from django.contrib import messages


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

def produto(request):
    context = {'produtos':Produto.objects.all()}
    return render(request, 'produtos/produtos.html',context)

def produto_detalhe(request, id_produto):
    produto = {'produto':Produto.objects.get(pk=id_produto)}
    return render(request, 'produtos/produto_detalhe.html', produto)
