from django.shortcuts import render
from produtos.forms import ProdutoForm

def new_product(request):
    if request.method != 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            return render(request, 'produtos/produto_form.html')
    form = ProdutoForm()
    context = {'form':form}
    return render(request, 'produtos/produto_form.html',context)

def produto(request):
    return render(request, 'produtos/produtos.html')