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
films = listings.find_all("a", title=True, limit=5)

home_url = "https://www.imdb.com"
# Loop each film and find selected data
for film in films:
    # Access each film page
    film_soup = make_soup(home_url + film["href"])

    title = film_soup.find("span", class_="sc-afe43def-1").text
    year = film_soup.find("ul", class_="kdXikI").find("a").text
    print(title, year)
