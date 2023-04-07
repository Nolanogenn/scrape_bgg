## BGG Scraping
### How to
Use get\_top\_100.py to retrieve the current top 100 from BGG. \
This code creates a csv file and a json file in the .\files\ directory. By default, the json file is saved as "top\_100\_latest.json", while the csv file is saved as "bgg\_scrape\_top\_100\_{current date}.csv", so that if scraping regularly a new csv file is created every time the scraper is called, while the json file is overwritten. \
### Scraped Data
I use this script to daily scrape data from the top 100 of BGG. The results are found at [https://gnolano.xyz/data/files/](https://gnolano.xyz/data/files/)
