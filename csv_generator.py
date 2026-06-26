import pandas as pd
import random

frases = [
    "Amei o novo iPhone! #Apple",
    "Promoção imperdível da Nike! #Desconto",
    "Samsung lançou um celular incrível #Tech",
    "Adidas com ofertas incríveis hoje #Sale",
    "Apple anunciou novos recursos #Tecnologia",
    "Não gostei do atendimento da loja #Reclamação",
    "Nike lançou uma nova coleção #Moda",
    "Desconto de 50% em eletrônicos #Promoção",
    "Galaxy S30 é o melhor celular #Samsung",
    "Comprei um tênis novo da Adidas #Fashion"
]

dados = []

# quantidade de posts que deseja gerar
quantidade = 10000

for i in range(1, quantidade + 1):
    dados.append({
        "id": i,
        "texto": random.choice(frases)
    })

df = pd.DataFrame(dados)

df.to_csv("posts.csv", index=False)

print("CSV criado com sucesso!")