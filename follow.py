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

wordnum = random.randint(0,6)
if wordnum == 0:
    word = "フォロバ率"
elif wordnum == 1:
    word = "自動フォロバ"
elif wordnum == 2:
    word = "フォロバ自動"
elif wordnum == 3:
    word = "フォロバ"
elif wordnum == 4:
    word = "フォロバ100"
elif wordnum == 5:
    word = "フォロバ100％"
else:
    word = "フォロバします"
groupnum = random.randint(0,19)
followparams = {
    "q": word,
    "page": groupnum,
    "per_page": "20",
    }
req = session.get("https://api.twitter.com/1.1/users/search.json",params = followparams)
users = json.loads(req.text)
usernum = random.randint(0,19)
uname = users[usernum]["screen_name"]
print uname
session.post("https://api.twitter.com/1.1/friendships/create.json",data={"screen_name" : uname})
