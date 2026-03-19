from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .forms import ProdutoForm
from .models import Produto


class ProdutoModelTests(TestCase):
    def test_str_returns_name_and_price(self):
        produto = Produto.objects.create(nome="Notebook", preco=Decimal("3500.00"))

        self.assertEqual(str(produto), "Notebook (R$ 3500.00)")


class ProdutoFormTests(TestCase):
    def test_form_accepts_valid_data(self):
        form = ProdutoForm(data={"nome": "Mouse", "preco": "99.90"})

        self.assertTrue(form.is_valid())

    def test_form_rejects_missing_name(self):
        form = ProdutoForm(data={"nome": "", "preco": "99.90"})

        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)

    def test_form_exposes_expected_fields(self):
        form = ProdutoForm()

        self.assertEqual(list(form.fields.keys()), ["nome", "preco"])


class ProdutoViewsTests(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Teclado", preco=Decimal("199.90")
        )

    def test_lista_produtos_returns_page_and_item(self):
        response = self.client.get(reverse("lista_produtos"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "produtos/lista.html")
        self.assertContains(response, "Teclado")

    def test_criar_produto_persists_and_redirects(self):
        response = self.client.post(
            reverse("criar_produto"),
            {"nome": "Monitor", "preco": "1299.90"},
        )

        self.assertRedirects(response, reverse("lista_produtos"))
        self.assertTrue(Produto.objects.filter(nome="Monitor").exists())

    def test_criar_produto_invalid_does_not_persist(self):
        response = self.client.post(
            reverse("criar_produto"),
            {"nome": "", "preco": "1299.90"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "produtos/form.html")
        self.assertFalse(Produto.objects.filter(preco=Decimal("1299.90")).exists())

    def test_editar_produto_updates_existing_record(self):
        response = self.client.post(
            reverse("editar_produto", args=[self.produto.pk]),
            {"nome": "Teclado Mecanico", "preco": "249.90"},
        )

        self.assertRedirects(response, reverse("lista_produtos"))
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, "Teclado Mecanico")
        self.assertEqual(self.produto.preco, Decimal("249.90"))

    def test_excluir_produto_removes_record(self):
        response = self.client.post(reverse("excluir_produto", args=[self.produto.pk]))

        self.assertRedirects(response, reverse("lista_produtos"))
        self.assertFalse(Produto.objects.filter(pk=self.produto.pk).exists())
