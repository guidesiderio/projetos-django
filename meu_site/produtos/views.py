from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm
from django.core.paginator import Paginator

# Create your views here.

# READ (lista)
def lista_produtos(request):
    q = request.GET.get("q", "").strip()
    qs = Produto.objects.all().order_by("-criado_em")
    if q:
        qs = qs.filter(nome__icontains=q)

    paginator = Paginator(qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page_range = page_obj.paginator.get_elided_page_range(
        number=page_obj.number, on_each_side=1, on_ends=1
    )

    context = {
        "q": q,
        "page_obj": page_obj,
        "page_range": page_range,
        "total": paginator.count,
    }
    return render(request, "produtos/lista.html", context)

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

