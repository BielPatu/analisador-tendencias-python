# Projeto PBL - Análise de Posts

## Visão geral

Este projeto contém dois scripts Python simples para gerar e analisar dados de posts fictícios em formato CSV.

- `csv_generator.py`: gera um arquivo `posts.csv` com posts simulados.
- `app.py`: analisa o arquivo `posts.csv` usando Apache Spark para identificar hashtags e categorias de interesse.

## Arquivos principais

- `csv_generator.py`
  - Gera 10.000 registros fictícios de posts.
  - Cada registro contém um `id` e um campo `texto` com hashtags e termos relevantes.
  - Salva os dados no arquivo `posts.csv`.

- `app.py`
  - Cria uma sessão Spark usando `SparkSession`.
  - Lê `posts.csv` com cabeçalho e inferência de esquema.
  - Extrai hashtags e mapeia textos para categorias como `Tecnologia`, `Moda` e `Promoções`.
  - Soma a ocorrência de cada hashtag/categoria e imprime o resultado.

## Como usar

### Pré-requisitos

- Python 3.x
- `pandas`
- `pyspark`

### Instalar dependências

No Windows, usando um ambiente virtual e `pip`:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas pyspark
```

### Gerar o CSV

Execute:

```bash
python csv_generator.py
```

Isso cria o arquivo `posts.csv` no diretório do projeto.

### Rodar a análise

Execute:

```bash
python app.py
```

O script imprimirá no console uma lista de tuplas com a contagem de hashtags e categorias encontradas.

## Uso em Jupyter ou Google Colab

Em projetos de análise de dados, é muito comum usar Jupyter Notebook ou Google Colab para:

- experimentar com dados interativamente
- visualizar resultados imediatamente
- documentar os passos de análise

Se você preferir, copie o conteúdo de `csv_generator.py` e `app.py` para células em um notebook, gere o `posts.csv` e execute a análise passo a passo.


## Resultado esperado

O `app.py` deve exibir algo como:

```python
[('#apple', 2), ('#desconto', 2), ('#tech', 1), ... , ('Tecnologia', 3), ('Moda', 3), ('Promoções', 3)]
```

Isso mostra a contagem de hashtags e categorias encontradas no conjunto de posts.
