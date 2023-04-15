from bs4 import BeautifulSoup
from csv import writer
import requests

# URL to web page
url = "https://www.rumah123.com/sewa/bandung/rumah/"
# Get HTML of the page, use headers to resolve denied '403' status code
page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})

# Parse HTML using BS
soup = BeautifulSoup(page.content, "html.parser")

# Find all sections of data
listings = soup.find_all("div", class_="card-featured__content-wrapper")

# Open csv file to be writen
with open("House_listings.csv", "w", encoding="utf8", newline="") as f:
    # Create writer object
    write = writer(f, delimiter=";")
    # Write header of the data table
    header = ["Title", "Location", "Price", "Description"]
    write.writerow(header)

    # Loop each section and find selected data
    for section in listings:
        title = section.find("a")["title"]
        location = section.find("span").text
        price = section.find("strong").text
        description = section.find("p").text.replace("\r", "")

        # Write into CSV file
        info = [title, location, price, description]
        write.writerow(info)