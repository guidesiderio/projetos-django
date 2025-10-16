<!--
Arquivo gerado/atualizado por um agente. Objetivo: instruir modelos/IA a trabalhar neste repositório Django pequeno.
-->
# Instruções rápidas para agentes (meu_site)

Se você é um agente codando neste repositório, foque nas informações concretas abaixo — elas descrevem a arquitetura, convenções e exemplos que ajudam a ser imediatamente produtivo.

## Visão geral do projeto
- Projeto Django minimal: `manage.py` na raiz do diretório `meu_site` usa `meu_site.settings`.
- Banco: SQLite (arquivo `db.sqlite3`) — padrão de desenvolvimento.
- App principal: `produtos/` contém modelos, views, urls, forms, templates e admin.
- Static files: pasta `static/` na raiz; em `settings.py` `STATICFILES_DIRS` aponta para `BASE_DIR / "static"`.

## Arquitetura & fluxo importante
- URLs: raiz do projeto redireciona caminhos `produtos/` para `produtos.urls` (`meu_site/urls.py`). Use nomes de rota para links (ex.: `lista_produtos`, `criar_produto`, `editar_produto`, `excluir_produto`).
- Views: implementadas como funções em `produtos/views.py` seguindo CRUD clássico:
  - `lista_produtos(request)` — listagem com busca por query param `q`, paginação via `Paginator` e `page_obj`; template: `produtos/lista.html`.
  - `criar_produto`, `editar_produto` — usam `ProdutoForm` (`produtos/forms.py`) e `messages.success()` para feedback.
  - `excluir_produto` — confirmação via GET, exclusão via POST.
- Models: `Produto` em `produtos/models.py` (campos: `nome`, `preco`, `criado_em`). Admin registrado em `produtos/admin.py`.
- Templates: estão sob `produtos/templates/produtos/`. Há um `base.html` em `produtos/templates/base.html` que carrega Bootstrap via CDN e fornece blocos `title` e `content`. Prefira estender esse `base.html`.

## Convenções do projeto (observadas no código)
- Templates: blocos padrão: `{% block title %}` e `{% block content %}`. Mensagens do Django (variável `messages`) são renderizadas no `base.html` como alerts Bootstrap.
- Forms: `ModelForm` em `produtos/forms.py` com widgets Bootstrap (`class="form-control"`). Ao criar/editar, as views retornam `form` e `titulo` para o template `produtos/form.html`.
- Navegação e links: sempre use `{% url 'nome_da_rota' ... %}`; exemplos: `{% url 'editar_produto' p.id %}`.
- Paginação: use `Paginator` e `get_elided_page_range()` conforme `lista_produtos` (ver `produtos/views.py`) e mantenha query string `q` ao navegar pelas páginas (templates já usam `?q={{ q|urlencode }}&page={{ p }}`).

## Fluxo de desenvolvimento e comandos úteis
- Instalar dependências (repositório inclui `requeriments.txt`):
  - Use um virtualenv/venv. Arquivo lista `Django==5.2.7` e dependências mínimas.
- Comandos principais (PowerShell):
```
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requeriments.txt
python manage.py migrate
python manage.py runserver
```
- Quando for criar fixtures mínimas ou testar rapidamente, use o shell Django:
```
python manage.py shell
from produtos.models import Produto
Produto.objects.create(nome='Exemplo', preco=10.00)
```

## Padrões para PRs/edits do agente
- Respeitar URLs nomeadas e templates existentes — preferir estender `base.html` em vez de duplicar HTML.
- Alterações no modelo: fornecer migrações (`python manage.py makemigrations`) e explicar impact
  o em `db.sqlite3`. Não aplique migrações no banco existente sem instruções explícitas do maintainers.
- Mensagens de sucesso: seguir o padrão `messages.success(request, "Mensagem")` já usado nas views.
- Validação de formulários: confiar em `ModelForm.is_valid()` e, se necessário, adicionar validações no próprio `forms.py`.

## Pontos de integração e dependências
- Dependências externas: apenas Django (conforme `requeriments.txt`). Bootstrapped UI usa CDN para Bootstrap.
- Banco: SQLite — nenhum service externo.

## Exemplos rápidos (copiar/colar em contexto)
- Link para editar produto no template de lista:
  - `<a href="{% url 'editar_produto' p.id %}">Editar</a>`
- Uso de form na view `criar_produto`:
  - `form = ProdutoForm(request.POST); if form.is_valid(): form.save(); messages.success(request, "Produto criado com sucesso!")`

## Onde procurar para mais contexto
- `meu_site/settings.py` — configuração de static, apps instalados e banco.
- `meu_site/urls.py` — roteamento global (inclui `produtos.urls`).
- `produtos/views.py`, `produtos/forms.py`, `produtos/models.py`, `produtos/urls.py`, `produtos/templates/` — exemplos canônicos de padrões do projeto.

## O que evitar / observações detectáveis
- Não altere `STATICFILES_DIRS` nem `STATIC_URL` sem necessidade — o frontend usa `static/css/custom.css`.
- Não remova o uso de mensagens ou o padrão de navegação por nome de rota.

---
Se algo aqui estiver incompleto ou você precisar que eu detalhe um padrão (por exemplo, fluxo de deploy, testes automatizados, ou adicionar migrações), diga o que quer que eu adicione e eu atualizo este arquivo.
