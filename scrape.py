import requests
from bs4 import BeautifulSoup

url = "http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS"

r = requests.get(url)
c = r.content

soup = BeautifulSoup(c, "html.parser")
print(soup.prettify())
