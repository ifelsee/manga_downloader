import requests
import wget
from bs4 import BeautifulSoup
import time
import os 
import re

os.chdir("Attack On Titan")

def download_Chapters(r):
    soup  = BeautifulSoup(r.content, 'html.parser')
    manga_links = soup.find_all("img")
    for link in manga_links:
        if  link.get("data-src")!= None:
            full_link = str("https://"+link.get("data-src").split("//")[-1])
            full_link = full_link[:-1]
            chapter_num = full_link[-6:-4]
            have_chapther = False
            for dirs in os.listdir():
                if dirs[-3:] == "tmp":
                    os.remove(dirs)
                    print("tmp Silindi! Sağlam Dosya İndiriliyor")
                elif  dirs[:-4] == str(chapter_num) and dirs:
                    have_chapther = True
                    print("dirs num = ",dirs, "  chapter num = ", chapter_num )
            if full_link[-3:] == "jpg" and have_chapther == False:
                print("++++++++++++",chapter_num,"-----------------")
                print(" --  ",full_link[-3:])
                wget.download(full_link)            



def episode_finder_func(wtart_episode):
     
    episode_finder = True
    first_episode_finded = False
    episode = 1 
    episode_zero = 0

    while episode_finder:
        # !flag kabul etmedi
        if episode >= 1000 or episode >=100:
            r = requests.get("https://mangadenizi.com/manga/attack-on-titan/{episode}".format(episode = episode))
        else:       
            r = requests.get("https://mangadenizi.com/manga/attack-on-titan/{episode_zero}{episode}".format(episode_zero=episode_zero,episode = episode))
        if r.status_code == 200:
            print("bölüm bulundu ", episode)
            first_episode_finded = True
            have_episode = False
            for dirs in os.listdir():
                if dirs == str(episode):
                    have_episode = False

            if have_episode == False:
                try:
                    os.mkdir(str(episode))
                except:
                    print("Dosya yaratılamadı")    
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


def main():
    episode_finder_func(1)




