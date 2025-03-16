import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.ndtv.com/latest"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

headlines = [item.get_text(strip=True) for item in soup.select("h2 a")]

folder_name = "Web_Scrapper"
os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist

file_path = os.path.join(folder_name, "news_headlines.txt")

with open(file_path, "w", encoding="utf-8") as file:
    file.write("\n".join(headlines))  # Save each headline on a new line

print(f"✅ News headlines saved to {file_path}")
