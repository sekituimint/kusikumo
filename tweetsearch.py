#coding:utf-8
import sys
import random
import pandas as pd
import ssl
import json
from requests_oauthlib import OAuth1Session
import rauth

CONSUMER_KEY="pTcCc9OEgKd20XS9uuGgOXamY"
CONSUMER_SECRET="Yn5rOOG5TSYlZldZZywtdBFjKPYKm88Lb7MlEFDBCQ5TzDAC5U"
ACCESS_TOKEN="2598208740-4EXDnTNWmj9FnDdrt9QIeDY6lUNHO4hy4MPwSeL"
ACCESS_TOKEN_SECRET="Ok1IoEvn3jWOMeeKxmKrnU1UD55pEpf0JJ7BV3nl8FzxE"
session = rauth.OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
searchurl = "https://api.twitter.com/1.1/search/tweets.json?"

params = {
    "q": unicode(u"奇しくも"),
    "lang": "ja",
    "result_type": "recent",
    "count": "30"
    }
req = session.get(searchurl,params = params)
tweets = json.loads(req.text)

uname = ""
tweetid = ""
while(True):
    num = random.randint(0,30)
    if tweets["statuses"][num][u'user'][u'screen_name'] == "kisikumo_bot":
        #print "入った"
        continue
    else:
        if tweets["statuses"][num][u'text'][0] == 'R' and tweets["statuses"][num][u'text'][1] == 'T':
            uname = tweets["statuses"][num]['entities'][u'user_mentions'][0][u'screen_name']
        #    print "yes"
        else:
            uname = tweets["statuses"][num][u'user'][u'screen_name']
        #    print "no"
        tweetid = tweets["statuses"][num][u'id_str']
        #print tweets["statuses"][num][u'text']
        #print "https://twitter.com/" + uname + "/status/" + tweetid
        break    
retweeturl  = 'https://api.twitter.com/1.1/statuses/retweet/' + tweetid + '.json'
req = session.post(retweeturl,data={"trim_user":"true"})
req = session.post("https://api.twitter.com/1.1/friendships/create.json",data={"screen_name" : uname})
