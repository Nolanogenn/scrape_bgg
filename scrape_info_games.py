import requests
import pandas as pd
from bs4 import BeautifulSoup
import pprint
import json
import re

CLEANR = re.compile('<.*?>') 


class scrape_info_game:
    def __init__(self, url):
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, 'html.parser')
        self.url = url
    def get_info(self):
        info = self.soup.find_all("script")
        script = info[2]
        jsonStr = script.text.strip()
        jsonStr = jsonStr.split(';\n')
        jsonStr = jsonStr[10].strip()
        info = json.loads(jsonStr[23:])

        json_game = {
                "url" : self.url,
                "id" : info['item']['id'],
                "name" : info['item']['name'],
                "images" : info['item']['images'],
                "website" : info['item']['website'],
                "description" : clean_html(info['item']['description']),
                "short_description": info['item']['short_description'],
                "yearpublished" : info['item']['yearpublished'],
                "minplayers" : info['item']['minplayers'],
                "maxplayers" : info['item']['maxplayers'],
                "minplaytime" : info['item']['minplaytime'],
                "maxplaytime" : info['item']['maxplaytime'],
                "minage" : info['item']['minage'],
                "stats" : info['item']['stats'],
                "polls" : info['item']['polls'],
                "accessories" : info['item']['links']['boardgameaccessory'],
                "artist" : info['item']['links']['boardgameartist'],
                "category": info['item']['links']['boardgamecategory'],
                "designer" : info['item']['links']['boardgamedesigner'],
                "developer" : info['item']['links']['boardgamedeveloper'],
                "editor" : info['item']['links']['boardgameeditor'],
                "graphic_designer" : info['item']['links']['boardgamegraphicdesigner'],
                "honor" : info['item']['links']['boardgamehonor'],
                "mechanic" : info['item']['links']['boardgamemechanic'],
                "publisher" : info['item']['links']['boardgamepublisher'],
                "sculptor" : info['item']['links']['boardgamesculptor'],
                "solodesigner" : info['item']['links']['boardgamesolodesigner'],
                "subdomain" : info['item']['links']['boardgamesubdomain'],
                "writer" : info['item']['links']['boardgamewriter'],
                "containedin" : info['item']['links']['containedin'],
                "contains" : info['item']['links']['contains'],
                "expands" : info['item']['links']['expandsboardgame'],
                "reimplementation" : info['item']['links']['reimplementation'],
                "reimplements" : info['item']['links']['reimplements'],
                "videogamebg" : info['item']['links']['videogamebg']
                }    

        return json_game

def clean_html(html):
    cleantext = re.sub(CLEANR, '', html)
    return cleantext

if __name__ == '__main__':

    info = scrape_info_game("https://boardgamegeek.com/boardgame/174430/gloomhaven")
    info = info.get_info()
    

