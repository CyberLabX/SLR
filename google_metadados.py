#As vezes é necessário instalar o openpyxl
import csv
import random
import pandas as pd
import time
from pprint import pprint
from fp.fp import FreeProxy
from scholarly import scholarly, ProxyGenerator

publications = []

# Query no Google Acadêmico
query = '("single source of truth" OR "source of truth" OR "integrated network management") AND (("zero touch network" OR "zero-touch network" OR "zero touch configuration" OR "zero touch management" OR "zero-touch management") OR ("network automation" OR "autonomous networks"))'
proxy = ProxyGenerator()
scholarly.use_proxy(proxy)

# Coletar dados dos artigos
pubs = scholarly.search_pubs(query)

for i, pub in enumerate(pubs):
    print('Artigo-' + str(i) + ' : ' + pub['bib'].get('title', 'NoTitle'))
    publication = {}
    publication['title'] = pub['bib'].get('title', 'NoTitle')
    publication['pub_year'] = pub['bib'].get('pub_year', 'NoDate')
    publication['abstract'] = pub['bib'].get('abstract', 'NoAbstract')
    publication['pub_url'] = pub['bib'].get('pub_url', 'NoURL')
    publications.append(publication)
    delay = random.randint(3, 10)
    time.sleep(delay)

# with open("jeronimo_google.csv", "w", newline="") as f:
#     w = csv.DictWriter(f, publications.keys())
#     w.writeheader()
#     w.writerow(publications)


df = pd.DataFrame(publications)
# Write DataFrame to Excel file
df.to_excel('outputs/jeronimo_google.xlsx', index=False)

print("Planilha criada com sucesso!")

# for i, result in enumerate(search_results):
#     try:
#         # Extrair título, ano e resumo
#         #print (result)
#         print(i)
#         #exit()
#         titulo = result['bib'].get('title', 'Sem título')
#         ano = result['bib'].get('pub_year', 'Sem ano')
#         resumo = result['bib'].get('abstract', 'Sem resumo')
#         #local= result['bib'].get('journal','local de publicação não encontrado')
#         link_para_o_texto=result.get( 'eprint_url','privado')
#         link_para_o_local= result['pub_url']
#         # Adicionar à lista
#         artigos.append({'Nome do Artigo': titulo, 'Ano': ano, 'Resumo': resumo, 'Link público do texto': link_para_o_texto, 'Link do repositorio de busca':link_para_o_local})
#         print(f'{i + 1}: {titulo} (Ano: {ano}) (Link público do texto: {link_para_o_texto}) (Link do repositorio de busca {link_para_o_local})')  # Exibir progresso
#         exit()
#         if i >= 20:
#             time.sleep(60)  # Limitar a 20 artigos para evitar sobrecarga
#             break
#     except Exception as e:
#         print(f"Erro no artigo {i + 1}: {e}")

# Converter para DataFrame e salvar em Excel
# df = pd.DataFrame(pubs)
# df.to_excel('artigos_sml_cybersecurity.xlsx', index=False)