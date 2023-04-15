from bs4 import BeautifulSoup
import requests

url = "https://www.rumah123.com/sewa/bandung/rumah/"
page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})

soup = BeautifulSoup(page.content, "html.parser")

listings = soup.find_all("div", class_="card-featured__content-wrapper")

