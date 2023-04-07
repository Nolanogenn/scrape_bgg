## BGG Scraping
### How to

Use get\_top\_100.py to retrieve the games in the current top 100 from [BGG](https://boardgamegeek.com/).


By default, the code creates two file in the ```files``` directory:
* ```top_100_latest.json```
* ```bgg_top_100_{current date}.csv```
Since the filename for the csv file depends on the date in which the file is created, if scraping regularly a new csv file is created every time the scraper is called. The json file, on the other hand, keeps track of the most recent state of data.


### Scraped Data

I use this script to daily scrape data from the top 100 of BGG. The results can be accessed [here](https://gnolano.xyz/data/files/).
