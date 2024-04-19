import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import json

header = {"Accept-Language": "en-US,en;q=0.5"}
header2 = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"}

movie_name = []
year = []
time = []
rating = []
metascore = []
votes = []

pages = np.arange(1,100,10)

for page in pages:
    print(f"Scraping page {page}...")
    page = requests.get("https://www.imdb.com/search/title/?groups=top_100&count=100&sort=user_rating,desc")
    print(f"Page status code: {page.status_code}")
    soup = BeautifulSoup(page.text, 'html.parser')
    movie_data = soup.findAll('div', attrs= {'class': 'ipc-metadata-list-summary-item'})
    print(f"Number of movie data found: {len(movie_data)}")
    sleep(randint(2,8))
    for store in movie_data:
        name = store.h3.a.text
        movie_name.append(name)
        print(f"Movie name: {name}")
        
        year_of_release = store.h3.a.find('span', class_ = "sc-b189961a-8 kLaxqf dli-title-metadata-item").text
        year.append(year_of_release)
        print(f"Year of release: {year_of_release}")
        
        runtime = store.p.find("span", class_ = "sc-b189961a-8 kLaxqf dli-title-metadata-item").text
        time.append(runtime)
        print(f"Runtime: {runtime}")
        
        RATe = store.find('div', class_= "sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").text.replace('\n', ' ')
        rating.append(RATe)
        print(f"Rating: {RATe}")
        
        MEta = store.find('span', class_= "sc-b189961a-11 csCMBE").text if store.find('span', class_="sc-b189961a-11 csCMBE") else "*****"
        metascore.append(MEta)
        print(f"Metascore: {MEta}")
        
        value = store.find_all('span', attrs = {'name': "nv"})
        voting=value[0].text
        votes.append(voting)
        print(f"Votes: {voting}")

print("Scraping completed.")

movie_list = pd.DataFrame({"Movie Name": movie_name, "Release Year": year, "Run-time": time, "Rating": rating, "Metascore": metascore, "Votes": votes})

movie_list.to_json("DATA-SET.json", orient="records", indent=4)
print("Data saved to 'DATA-SET.json'.")
