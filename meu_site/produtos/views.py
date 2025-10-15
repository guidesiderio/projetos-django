from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.order_by("-criado_em")
    return render(request, "produtos/lista.html", {"produtos": produtos})

# READ (lista)
def lista_produtos(request):
    produtos = Produto.objects.order_by("-criado_em")
    return render(request, "produtos/lista.html", {"produtos": produtos})

# CREATE
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto criado com sucesso!")
            return redirect("lista_produtos")
    else:
        form = ProdutoForm()
    return render(request, "produtos/form.html", {"form": form, "titulo": "Novo produto"})

# UPDATE
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect("lista_produtos")
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "produtos/form.html", {"form": form, "titulo": "Editar produto"})

# DELETE (confirmação + exclusão)
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect("lista_produtos")
    return render(request, "produtos/confirm_delete.html", {"produto": produto})

