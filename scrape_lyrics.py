from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

# Create a session for persistent requests
session = requests.Session()

# Set the artist name (change this to target a different artist)
artist_name = "taylor-swift"

# Build the artist URL
artist_url = f"https://www.letras.mus.br/{artist_name}/"

# Request the artist page and parse it
response = session.get(artist_url)
soup = BeautifulSoup(response.content, "lxml")

# Extract all song links from the artist page
song_links = [tag["href"] for tag in soup.find_all("a", class_="songList-table-songName")]

# List to hold all scraped data
scraped_data = []

# Loop through each song link and collect metadata
for song_link in tqdm(song_links, desc="Scraping lyrics"):
    song_url = f"https://www.letras.mus.br{song_link}"
    song_response = session.get(song_url)
    song_soup = BeautifulSoup(song_response.content, "lxml")

    try:
        title = song_soup.find("h1", class_="head-title").text.strip()
        lyrics = song_soup.find("div", class_="lyric-original").text.strip()

        views_tag = song_soup.find("div", class_="head-info-exib")
        views = 0
        if views_tag and views_tag.find("b"):
            views = int(views_tag.find("b").text.strip().replace(".", "").replace(",", ""))

        scraped_data.append({
            "Title": title,
            "Lyrics": lyrics,
            "Link": song_url,
            "Artist": artist_name,
            "Views": views
        })

    except AttributeError:
        print(f"[!] Missing data on page: {song_url}")

# Create DataFrame
df = pd.DataFrame(scraped_data)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Export to Excel
excel_filename = f"{artist_name}_lyrics.xlsx"
df.to_excel(excel_filename, index=False)
print(f"[✓] Lyrics saved to '{excel_filename}'")
