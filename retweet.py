import re
import json
from requests_oauthlib import OAuth1Session


CONSUMER_KEY = "Je5WxQ7r7TdLZy7b8zCnkXURR"
CONSUMER_SECRET = "fqoluX4XuwCusc9UHE0T99N6YtAcw9jUZ4kezM362AluSKT3Dg" 
ACCESS_TOKEN = "1231510079125409793-OcTlpR6BEAiNvifL0YBb4TkFuw3cLt"
ACCESS_TOKEN_SECRET = "CRcXY7e2icV3kFHlQjaCENa3FAnaj8CX1otOQYaDeWGAr"

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def RT(id):
    END_POINT_BASE_URL = "https://api.twitter.com/1.1/statuses/retweet/"
    end_point_url = END_POINT_BASE_URL + id +".json"
    res = twitter.post(end_point_url)#リツイート処理
    return res

def unRT(id):
    END_POINT_BASE_URL = "https://api.twitter.com/1.1/statuses/unretweet/"
    end_point_url = END_POINT_BASE_URL + id +".json"
    res = twitter.post(end_point_url)#リツイート取り消し処理


url_list = [
    "https://twitter.com/mikansei_corn/status/1231552816121970688",
    "https://twitter.com/mikansei_corn/status/1230947608488636416",
    "https://twitter.com/mikansei_corn/status/1231795697684402177"
]
#params = {'id':1230947608488636416}

id_list = [re.search(r"\d+$", url).group() for url in url_list]

for  id in id_list:
    unRT(id)
    res = RT(id)
    print(res.status_code)
    retweet = json.loads(res.text)
    print(retweet["text"])