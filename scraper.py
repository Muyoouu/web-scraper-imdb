from bs4 import BeautifulSoup
import requests

def make_soup(url):
    # Get HTML of the page, use headers to resolve denied '403' status code
    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})

    # Parse HTML using BS
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

# URL to web page
url = "https://www.imdb.com/chart/top/"
soup = make_soup(url)

# Find the films listings
listings = soup.find("tbody", class_="lister-list")
# Find the link to each film detailed page, limit to 5 for this project
films = listings.find_all("a", limit=5)

"""
# Loop each section and find selected data
for film in films:
    # Access each film page
    film_soup = make_soup(film["href"])

    title = section.find("a")["title"]
    location = section.find("span").text
    price = section.find("strong").text
    description = section.find("p").text.replace("\r", "")

    # Write into CSV file
    info = [title, location, price, description]

"""