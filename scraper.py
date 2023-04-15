from bs4 import BeautifulSoup
from csv import writer
import requests

url = "https://www.rumah123.com/sewa/bandung/rumah/"
page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})

soup = BeautifulSoup(page.content, "html.parser")

listings = soup.find_all("div", class_="card-featured__content-wrapper")

with open("House_listings.csv", "w", encoding="utf8", newline="") as f:
    write = writer(f, delimiter=";")
    header = ["Title", "Location", "Price", "Description"]
    write.writerow(header)

    for section in listings:
        title = section.find("a")["title"]
        location = section.find("span").text
        price = section.find("strong").text
        description = section.find("p").text.replace("\r", "")

        info = [title, location, price, description]
        write.writerow(info)