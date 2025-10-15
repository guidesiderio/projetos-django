from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "preco"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Notebook"}),
            "preco": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }
        labels = {
            "nome": "Nome do produto",
            "preco": "Preço (R$)",
        }
