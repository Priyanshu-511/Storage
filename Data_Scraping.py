import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import json
import re

url = 'https://www.imdb.com/search/title/?groups=top_250&count=250&sort=user_rating,desc'
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    }
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
year = []
runtime = []
score = []
votes = []
summary = []

movie_data = soup.findAll('div', attrs= {'class' : 'ipc-metadata-list-summary-item__c'})
for store in movie_data:
    Name = store.find('h3', class_= 'ipc-title__text').text
    movie_name.append(Name)
    
    RElease = store.find('span', class_="sc-b189961a-8 kLaxqf dli-title-metadata-item").text
    year.append(RElease)

    time = store.find('div', class_="sc-b189961a-7 feoqjK dli-title-metadata").text
    runtime.append(time[4:].strip())

    rating_span  = store.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
    rating_text = rating_span.text
    imdb_rating = rating_text.split('\xa0')[0]
    score.append(imdb_rating)
    
    vote_span  = store.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
    vote_text = vote_span.text
    vote_count = re.search(r'\((.*?)\)', vote_text).group(1)
    votes.append(vote_count)
    
    story = store.find('div', class_="sc-ab6fa25a-1 bBwFsP").text
    summary.append(story)

movie_to = pd.DataFrame({"Movie Name": movie_name, "Year": year, "Run time & Rated": runtime, "IMDb-Rating": score, "Voting": votes, "Summary":summary})

movie_to.to_json("DATA-SET.json", orient="records", indent=4)

print("scrapping done!")