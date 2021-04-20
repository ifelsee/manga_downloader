import requests
import wget
from bs4 import BeautifulSoup
import time
import os 

episode_find = True
episode = 760
episode_zero = 0
while episode_find:
    
    r = requests.get("https://mangadenizi.com/manga/one-piece/{episode_zero}{episode}".format(episode_zero=episode_zero,episode = episode))
    if r.status_code == 200:
        print("bölüm bulundu")
        episode_find = False
    else: episode = episode +1
    print("{episode_zero}{episode}".format(episode_zero=episode_zero,episode = episode))
