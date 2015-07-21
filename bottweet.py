#coding:utf-8
import sys
import random
import pandas as pd
import ssl
import json
from requests_oauthlib import OAuth1Session
import rauth
#from twitter import *

CONSUMER_KEY="Isq3KSGESWa0ifwQa7LonN5OV"
CONSUMER_SECRET="FnkGwNgtIS2nLAI4nDSuprPwq9iH2clXpGmLxr06OhcXF6J6HM"
ACCESS_TOKEN="3283844030-fxNvnsLAx527m8FkeXYah1kvuA8nH0fGPXwVV28"
ACCESS_TOKEN_SECRET="weWJZ5hI4FguLLrOjg0oUio63UCUvXGl2c6kOAprBPR1G"
session = rauth.OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

tweeturl = "https://api.twitter.com/1.1/statuses/update.json"

word = random.randint(0,6)
if word == 0:
    tweettext = "ツイッター初心者です！みんなと繋がりたい！！"
elif word == 1:
    tweettext = "フォロワーさんいっぱい繋がりたい！！"
elif word == 2:
    tweettext = "ツイッター初心者ですフォローお願いします！！！！"
elif word == 3:
    tweettext = "アニメ・マンガ大好き！！一緒に語りたい！！"
elif word == 4:
    tweettext = "アニメ・マンガ大好きです！フォローお願いします！！"
elif word == 5:
    tweettext = "ツイッターで一緒にアニメ・マンガを語りたい！！よろしくお願いします！！"
else:
    tweettext = "ツイッター初心者です！！アニメマンガ語れる友達がほしい！！！"     

wordnum = random.randint(2,6)
words = []
while(True):
    word = random.randint(0,6)
    if word == 0:
        tweetword = "\n#相互希望"
    elif word == 1:
        tweetword = "\n#RTした人全員フォローする"
    elif word == 2:
        tweetword = "\n#RTした人フォローする"
    elif word == 3:
        tweetword = "\n#相互フォロー"
    elif word == 4:
        tweetword = "\n#teamfollowback"
    elif word == 5:
        tweetword = "\n#ふぁぼした人全員フォローする"
    else:
        tweetword = "\n#拡散希望"
    if (tweetword in words) == False:
        tweettext = tweettext + tweetword
        words.append(tweetword)
        wordnum -= 1
    if wordnum == 0:
        break
print tweettext
res = session.post(tweeturl, data={'status': tweettext})
#while(True):
#    rand = random.randint(0,len(df['tweets']))
#    if df['length'][rand] < 140:
#
#        if res.status_code == 200:
#            print "そう"
#            print df['tweets'][rand].decode("shift-jis")
#            break
#        else:
#            print "違う"
#            print res.status_code
#            print df['tweets'][rand].decode("shift-jis")

