from django.shortcuts import render

# Create your views here.

from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.order_by("-criado_em")
    return render(request, "produtos/lista.html", {"produtos": produtos})
