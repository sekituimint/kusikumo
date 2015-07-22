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
followlist = follows["ids"]

req= session.get("https://api.twitter.com/1.1/statuses/home_timeline.json",params = {"count":"200"})
timelines = json.loads(req.text)
uid = ""
tweetid = ""
while(True):
    num = random.randint(0,198)
    if timelines[num]["text"][0] == 'R' and timelines[num]["text"][1] == 'T':
        if u"はRT" in timelines[num]["text"] or u"人RT" in timelines[num]["text"] or u"繋がりたい" in timelines[num]["text"]:
            if timelines[num]["user"]["id_str"] in follows["ids"]:
                print "フォローしてた"
            elif timelines[num]["user"]["screen_name"] == "H_I_R_A_I_I":
                print "自分だった"
            else:
                #print "フォローしてなかった"
                uid = timelines[num]['entities']['user_mentions'][0]["id_str"]
                tweetid = timelines[num]["id_str"]
                #print timelines[num]["text"]
                break
    #print "違う"
    continue

if uid != "":
    #print uid
    #print tweetid
    retweeturl  = 'https://api.twitter.com/1.1/statuses/retweet/' + tweetid + '.json'
    req = session.post(retweeturl,data={"trim_user":"true"})
    req= session.get("https://api.twitter.com/1.1/users/lookup.json",params = {"user_id": uid })
    detail = json.loads(req.text)
    uname = detail[0]["screen_name"]
    #print uname
    req = session.post("https://api.twitter.com/1.1/friendships/create.json",data={"user_id" : uid})
    tweetstr = "@"  + str(uname)+ " RTさせて頂きました！ぜひ相互フォローよろしくお願いします！！"
    print tweetstr
    req = session.post("https://api.twitter.com/1.1/statuses/update.json",data={"status" : tweetstr})
