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

req = session.get("https://api.twitter.com/1.1/friends/ids.json",params = {})
follows = json.loads(req.text)
req = session.get("https://api.twitter.com/1.1/followers/ids.json",params = {})
followers = json.loads(req.text)

print len(follows["ids"])
followlist = follows["ids"]
followlist.reverse()
count = 0
while(True):
    if (followlist[count] in followers["ids"]) == False:
        print followlist[count]
        uid = followlist[count]
        break
    count+=1
    if count == len(follows["ids"]) - 10:
        break

req = session.post("https://api.twitter.com/1.1/friendships/destroy.json",data={"user_id" : uid})
print req
