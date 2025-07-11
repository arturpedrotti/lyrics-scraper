# 🎵 Song Lyrics Scraper 🎶

## 📋 Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Author](#author)
6. [Acknowledgments](#acknowledgments)

---

## 🎤 Overview

This project is a Python-based tool that scrapes song lyrics and metadata from [Letras.mus.br](https://www.letras.mus.br/). It allows users to:

- Fetch all lyrics from a specific artist
- Collect the number of views for each song
- Export the results to an Excel file

It's a simple and powerful utility for music enthusiasts and data nerds.

---

## ⚙️ Installation

Make sure you have **Python 3.x** installed.

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the script:

```bash
python3 scrape_lyrics.py
```

To scrape lyrics for a different artist, edit the `artist_name` variable inside the script:

```python
artist_name = "your-artist-name"
```

Use the URL-friendly version of the artist's name as it appears on [letras.mus.br](https://www.letras.mus.br/).

---

## ✨ Features

- Scrapes lyrics and metadata for all songs by a given artist
- Collects total view count per song
- Exports clean, deduplicated data to an Excel file

---

## 👤 Author

- [@arturpedrotti](https://github.com/arturpedrotti)

---

## 🙏 Acknowledgments

Special thanks to [@mateuspestana](https://github.com/mateuspestana) for the original inspiration and guidance on this project.
