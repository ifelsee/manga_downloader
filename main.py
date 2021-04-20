import requests
import wget
from bs4 import BeautifulSoup
import time
import os 

episode_finder = True
first_episode_finded = False
episode = 700
episode_zero = 0

os.chdir("One Piece")

def download_Chapters(r):
    soup  = BeautifulSoup(r.content, 'html.parser')
    manga_links = soup.find_all("img")
    for link in manga_links:
        if  link.get("data-src")!= None:
            full_link = str("https://"+link.get("data-src").split("//")[-1])
            full_link = full_link[:-1]
            print(full_link[-3:])
            if full_link[-3:] == "jpg":
                wget.download(full_link)            


def main():
    while episode_finder:
        # !flag kabul etmedi
        if episode >= 1000: 
            r = requests.get("https://mangadenizi.com/manga/one-piece/{episode}".format(episode = episode))
        else:       
            r = requests.get("https://mangadenizi.com/manga/one-piece/{episode_zero}{episode}".format(episode_zero=episode_zero,episode = episode))
        if r.status_code == 200:
            print("bölüm bulundu ", episode)
            first_episode_finded = True
            os.mkdir(str(episode))
            os.chdir(str(episode)) 
            download_Chapters(r)
            os.chdir("../")
            episode = episode +1
        elif r.status_code == 500:
            if first_episode_finded == True:
                print("Başka bölüm bulunamadı ", episode)
                episode_finder = False
            else:
                print("bölüm bulunamadı ", episode)
                episode = episode +1
        else: episode = episode +1
