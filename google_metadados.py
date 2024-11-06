#As vezes é necessário instalar o openpyxl

import pandas as pd
import time
from scholarly import scholarly

# Query no Google Acadêmico
search_query = ' ("machine learning" OR "artificial intelligence" OR "AI") AND ("synthetic data" OR "Data Augmentation" ) AND ("tabular data") AND ("cybersecurity" OR "cyber security")'

# Coletar dados dos artigos
artigos = []
search_results = scholarly.search_pubs(search_query)

for i, result in enumerate(search_results):
    try:
        # Extrair título, ano e resumo
        #print (result)
        print(i)
        #exit()
        titulo = result['bib'].get('title', 'Sem título')
        ano = result['bib'].get('pub_year', 'Sem ano')
        resumo = result['bib'].get('abstract', 'Sem resumo')
        #local= result['bib'].get('journal','local de publicação não encontrado')
        link_para_o_texto=result.get( 'eprint_url','privado')
        link_para_o_local= result['pub_url']
        # Adicionar à lista
        artigos.append({'Nome do Artigo': titulo, 'Ano': ano, 'Resumo': resumo, 'Link público do texto': link_para_o_texto, 'Link do repositorio de busca':link_para_o_local})
        print(f'{i + 1}: {titulo} (Ano: {ano}) (Link público do texto: {link_para_o_texto}) (Link do repositorio de busca {link_para_o_local})')  # Exibir progresso
        exit()
        if i >= 20:
            time.sleep(60)  # Limitar a 20 artigos para evitar sobrecarga
            break
    except Exception as e:
        print(f"Erro no artigo {i + 1}: {e}")

# Converter para DataFrame e salvar em Excel
df = pd.DataFrame(artigos)
df.to_excel('artigos_sml_cybersecurity.xlsx', index=False)

print("Planilha criada com sucesso!")