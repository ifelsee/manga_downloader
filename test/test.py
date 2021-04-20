import requests 
import wget
from bs4 import BeautifulSoup
import time
r = requests.get("https://mangadenizi.com/manga/one-piece/0765")

soup  = BeautifulSoup(r.content, 'html.parser')

manga_links = soup.find_all("img")
for link in manga_links:
    if  link.get("data-src")!= None:
        full_link = str("https://"+link.get("data-src").split("//")[-1])
        full_link = full_link[:-1]
        print(full_link[-3:])
        if full_link[-3:] == "jpg"
        wget.download(full_link)            

