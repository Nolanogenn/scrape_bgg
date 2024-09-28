import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
from scrape_info_games import scrape_info_game
import json
from tqdm import tqdm


class scrape_bgg:
    def __init__(self):
        self.columns = [
                        'standing', 
                        'title',
                        'year',
                        'description', 
                        'geek_rating',
                        'avg_rating',
                        'num_voters',
                        'url'
                        ]
        url = "https://boardgamegeek.com/browse/boardgame"
        self.today = date.today()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table', attrs = {"class" : "collection_table"})
        self.rows = table.find_all('tr')
        pages_to_scrape = range(1,6) 
        for page in pages_to_scrape:
            additional_url = url + f"/page/{page}"
            additional_rows = table.find_all('tr')
            self.rows.extend(additional_rows)
    def clean_title(self, string_title):
        string_title = string_title.split('\n')
        title = string_title[0]
        year = int(string_title[1][1:-1])
        description = string_title[4].replace('\t', '')
        return title, year, description

    def get_df_and_json(self):
        df = []
        json_file = []

        for row in tqdm(self.rows):
            cols = row.find_all('td')
            cols_url = [ele for ele in cols]
            cols_elem = [ele.text.strip() for ele in cols]
            cols_elem = [ele for ele in cols_elem if cols][:-1]
            if len(cols_elem) > 0:

                url_tailing = cols_url[2].find_all('a', href=True)[0]['href']
                url = "https://boardgamegeek.com/{}".format(url_tailing)
            
                place = int(cols_elem[0])
                title, year, description = self.clean_title(cols_elem[2])
                geek_rating = float(cols_elem[3])
                avg_rating = float(cols_elem[4])
                num_voters = int(cols_elem[5])
                
                row_clean = [place,title, year, description, geek_rating, avg_rating, num_voters, url]
                df.append(row_clean)
                
                dict_game = scrape_info_game(url)
                dict_game = dict_game.get_info()

                json_file.append(dict_game)

        df = pd.DataFrame(df, columns = self.columns)
        filename = './files/bgg_scrape_top1000_{}'.format(self.today)
        

        df.to_csv(f"{filename}.csv")
        with open(f"./files/top_1000_latest.json", 'w+') as f:
            json.dump(json_file, f)

if __name__ == '__main__':
    print("scraping the top 1000 from bgg...")
    ws = scrape_bgg()
    ws.get_df_and_json()
    print("done!")
