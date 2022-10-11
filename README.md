# CNAB Upload

Pequena aplicação para upload de arquivo CNAB e armazenamento em um banco de dados relacional.

## Documentação da API

#### Post um item.

```http
  POST /uploadfile/
```

| Tipo             | Descrição                  |
| :--------------- | :------------------------- |
| `multipart/form` | **Obrigatório**. CNAB File |

#### Retorna uma lista de transações por loja.

```http
  GET /transactions/
```

| Parâmetro      | Tipo                                    |
| :------------- | :-------------------------------------- |
| `id`           | `uuid`                                  |
| `transactions` | `Obj {total: string, transactions: []}` |
| `store_owner`  | `string`                                |
| `store_name`   | `string`                                |
| `cpf`          | `string`                                |

## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:danilovalerio89/cnab-kenzie.git
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  ./manage.py runserver
```

## Melhorias

Encontrar uma outra maneira de fazer upload e salvar os arquivos.

## Aprendizados

Primeiro contato com Upload de arquivos com o django-restframework.
