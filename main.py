from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL do site
site = 'https://www.globo.com'
response = requests.get(site)
soup = BeautifulSoup(response.content, 'html.parser')

# Listas para armazenar títulos e links
all_titles = []
all_links = []

# Coleta dos títulos
titles = soup.find_all('h2', class_='post__title')
for title in titles:
    all_titles.append(title.get_text(strip=True))  # Extraindo o texto do título

# Coleta dos links
links = soup.find_all('a', class_='post__link')
for link in links:
    href = link.get('href')  # Extraindo o atributo href do link
    if href:  # Verifica se o href não é None
        all_links.append(href)

# Cria um DataFrame
dados = {'titulos': all_titles[:len(all_links)], 'links': all_links}  # Fazendo o corte para ter o mesmo comprimento
df = pd.DataFrame(dados)

# Salva o DataFrame como um arquivo CSV
df.to_csv('titulos_e_links.csv', index=False)

print("Arquivo CSV criado com sucesso!")
