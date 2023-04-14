from bs4 import BeautifulSoup
import requests

url = "https://www.rumah123.com/sewa/bandung/rumah/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

listings = soup.find_all("div", class_="card-featured__content-wrapper")

# for section in listings:
#     title = section.find("a", )