#coding:utf-8
import sys
import random
import pandas as pd
import ssl
import json
from requests_oauthlib import OAuth1Session
import rauth
#from twitter import *



CONSUMER_KEY="pTcCc9OEgKd20XS9uuGgOXamY"
CONSUMER_SECRET="Yn5rOOG5TSYlZldZZywtdBFjKPYKm88Lb7MlEFDBCQ5TzDAC5U"
ACCESS_TOKEN="2598208740-4EXDnTNWmj9FnDdrt9QIeDY6lUNHO4hy4MPwSeL"
ACCESS_TOKEN_SECRET="Ok1IoEvn3jWOMeeKxmKrnU1UD55pEpf0JJ7BV3nl8FzxE"

session = rauth.OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
tweeturl = "https://api.twitter.com/1.1/statuses/update.json"

df = pd.read_csv('kisikumo_list.csv')
while(True):
    rand = random.randint(0,len(df['tweets']))
    if df['length'][rand] < 140:
        res = session.post(tweeturl, data={'status': df['tweets'][rand].decode("shift-jis")})
        if res.status_code == 200:
            print "そう"
            print df['tweets'][rand].decode("shift-jis")
            break
        else:
            print "違う"
            print res.status_code
            print df['tweets'][rand].decode("shift-jis")

