from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

# Crie uma sessão
session = requests.Session()

# Artista escolhido (Mude o nome do artista de acordo com sua preferência)
artist_name = "taylor-swift"

# URL do artista
artist_url = f'https://www.letras.mus.br/{artist_name}/'

# Faça a requisição inicial para obter a lista de músicas
response = session.get(artist_url)
soup = BeautifulSoup(response.content, 'lxml')

# Encontrar todas as músicas
song_links = [tag['href'] for tag in soup.find_all('a', {'class': 'songList-table-songName'})]

# Lista para armazenar as informações raspadas
scraped_data = []

# Loop para cada música
for song_link in tqdm(song_links):
    song_url = f'https://www.letras.mus.br{song_link}'
    song_response = session.get(song_url)
    song_soup = BeautifulSoup(song_response.content, 'lxml')
    
    try:
        title = song_soup.find('h1', {'class': 'head-title'}).text.strip()
        lyrics = song_soup.find('div', {'class': 'lyric-original'}).text.strip()
        views_tag = song_soup.find('div', {'class': 'head-info-exib'}).find('b')
        views = int(views_tag.text.strip().replace('.', '').replace(',', '')) if views_tag else 0

        song_data = {
            'Title': title,
            'Lyrics': lyrics,
            'Link': song_url,
            'Artist': artist_name,
            'Views': views
        }

        scraped_data.append(song_data)

    except AttributeError:
        print(f"Algum atributo não foi encontrado na página: {song_url}")

# Crie um DataFrame com os dados raspados
df = pd.DataFrame(scraped_data)

# Remova duplicatas
df.drop_duplicates(inplace=True)

# Salve o DataFrame em um arquivo Excel
excel_filename = f"{artist_name}_musicas.xlsx"
df.to_excel(excel_filename, index=False)
print(f"Arquivo '{excel_filename}' salvo com sucesso.")

