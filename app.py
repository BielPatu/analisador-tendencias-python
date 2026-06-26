import pandas as pd
import re
from collections import Counter

# Ler o CSV
dados = pd.read_csv("posts.csv")

# Contar hashtags e categorias
contador = Counter()

for texto in dados["texto"]:
    texto_lower = texto.lower()
    
    # Extrair hashtags
    hashtags = re.findall(r"#\w+", texto_lower)
    for h in hashtags:
        contador[h] += 1
    
    # Categorizar por palavras-chave
    if any(p in texto_lower for p in ["iphone", "apple", "samsung"]):
        contador["Tecnologia"] += 1
    
    if any(p in texto_lower for p in ["nike", "adidas"]):
        contador["Moda"] += 1
    
    if any(p in texto_lower for p in ["promoção", "desconto", "sale"]):
        contador["Promoções"] += 1

# Exibir resultados
print("\nResultados da Análise:")
print("=" * 50)
for chave, valor in contador.most_common():
    print(f"{chave}: {valor}")