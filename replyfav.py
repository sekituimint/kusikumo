#coding:utf-8
import sys
import random
import pandas as pd
import ssl
import json
from requests_oauthlib import OAuth1Session
import rauth

CONSUMER_KEY="Isq3KSGESWa0ifwQa7LonN5OV"
CONSUMER_SECRET="FnkGwNgtIS2nLAI4nDSuprPwq9iH2clXpGmLxr06OhcXF6J6HM"
ACCESS_TOKEN="3283844030-fxNvnsLAx527m8FkeXYah1kvuA8nH0fGPXwVV28"
ACCESS_TOKEN_SECRET="weWJZ5hI4FguLLrOjg0oUio63UCUvXGl2c6kOAprBPR1G"
session = rauth.OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
searchurl = "https://api.twitter.com/1.1/search/tweets.json?"

req = session.get("https://api.twitter.com/1.1/statuses/mentions_timeline.json",params = {"count":"50"})

mentions = json.loads(req.text)
count = 0
for i in range(5):
    if mentions[i]["favorited"] == False:
        url  = 'https://api.twitter.com/1.1/favorites/create.json'
        req = session.post(url,data={"id":mentions[i]["id_str"]})
        print "fav"
        print req


