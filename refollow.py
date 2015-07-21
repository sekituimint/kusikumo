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

params = {
    "q": unicode(u"#RTした人全員フォローする"),
    "lang": "ja",
    "result_type": "recent",
    "count": "100"
    }
req = session.get(searchurl,params = params)
tweets = json.loads(req.text)

req = session.get("https://api.twitter.com/1.1/friends/ids.json",params = {})
follows = json.loads(req.text)
req = session.get("https://api.twitter.com/1.1/followers/ids.json",params = {})
followers = json.loads(req.text)

print len(follows["ids"])
count = 0
while(True):
    num = random.randint(0,30)
    if followers["ids"][num] in follows["ids"]:
        print "False"
        count += 1
        if count == 30:
            break
        continue
    else:
        print "True"
        uid = followers["ids"][num]
        break
if uid != "":
    req = session.get("https://api.twitter.com/1.1/users/lookup.json",params = {"user_id": uid })
    detail = json.loads(req.text)
    uname = detail[0]["screen_name"]

    req = session.post("https://api.twitter.com/1.1/friendships/create.json",data={"user_id" : uid})
    tweetstr = "@"  + str(uname)+ " フォローありがとうございます！よろしくお願いします！！"
    req = session.post("https://api.twitter.com/1.1/statuses/update.json",data={"status" : tweetstr})
