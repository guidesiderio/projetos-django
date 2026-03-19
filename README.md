# DjangoShop

Projeto Django simples para cadastro e gerenciamento de produtos.

## Stack

- Python
- Django 5.2.7
- SQLite
- Bootstrap 5 via CDN

## Como executar

1. Crie e ative um ambiente virtual.
2. Instale as dependencias:

```powershell
pip install -r requirements.txt
```

3. Aplique as migracoes:

```powershell
python manage.py migrate
```

4. Crie um superusuario, se quiser acessar o admin:

```powershell
python manage.py createsuperuser
```

5. Rode o servidor:

```powershell
python manage.py runserver
```

6. Acesse:
   - `http://127.0.0.1:8000/produtos/`
   - `http://127.0.0.1:8000/admin/`

## Variaveis de ambiente

- `DJANGO_DEBUG`: controla o modo debug. Aceita valores como `True`, `False`, `1` e `0`.
- `DJANGO_SECRET_KEY`: obrigatoria em producao. Em desenvolvimento local existe um fallback inseguro apenas para facilitar setup local.
- `DJANGO_ALLOWED_HOSTS`: lista de hosts separados por virgula. Exemplo: `localhost,127.0.0.1,seu-dominio.com`.

## Testes

Rode os testes com:

```powershell
python manage.py test
```

## Dependencias

O projeto usa [`requirements.txt`](requirements.txt) como arquivo padrao de dependencias.
