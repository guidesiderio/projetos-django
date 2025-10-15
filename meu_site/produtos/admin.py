from django.contrib import admin

# Register your models here.

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "criado_em")
    search_fields = ("nome",)
    list_filter = ("criado_em",)