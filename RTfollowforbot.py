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
print follows["ids"][0]
print len(follows["ids"])
uname = ""
tweetid = ""
while(True):
    num = random.randint(0,99)
    if tweets["statuses"][num][u'text'][0] == 'R' and tweets["statuses"][num][u'text'][1] == 'T':
        uname = tweets["statuses"][num]['entities'][u'user_mentions'][0][u'screen_name']
        uid = tweets["statuses"][num]['entities'][u'user_mentions'][0]['id']
        print uid 
    else:
        uname = tweets["statuses"][num][u'user'][u'screen_name']
        uid = tweets["statuses"][num][u'user'][u'id']
        print uid
    if uid in follows["ids"]:
        print "やり直しいいいいいいいいいいいいいいいいいいい"
        continue
    else:
        tweetid = tweets["statuses"][num][u'id_str']
        print "入ったああああああああああああああああああああ"
        break    
retweeturl  = 'https://api.twitter.com/1.1/statuses/retweet/' + tweetid + '.json'
req = session.post(retweeturl,data={"trim_user":"true"})
req = session.post("https://api.twitter.com/1.1/friendships/create.json",data={"screen_name" : uname})
tweetstr = "@"  + str(uname)+ " はじめまして！twitter初心者なのですがぜひ相互フォローお願いします！"
req = session.post("https://api.twitter.com/1.1/statuses/update.json",data={"status" : tweetstr})
