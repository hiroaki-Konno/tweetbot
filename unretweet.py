import json
from requests_oauthlib import OAuth1Session


CONSUMER_KEY = "Je5WxQ7r7TdLZy7b8zCnkXURR"
CONSUMER_SECRET = "fqoluX4XuwCusc9UHE0T99N6YtAcw9jUZ4kezM362AluSKT3Dg" 
ACCESS_TOKEN = "1231510079125409793-OcTlpR6BEAiNvifL0YBb4TkFuw3cLt"
ACCESS_TOKEN_SECRET = "CRcXY7e2icV3kFHlQjaCENa3FAnaj8CX1otOQYaDeWGAr"

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

END_POINT_URL = "https://api.twitter.com/1.1/statuses/unretweet/1230947608488636416.json"

#params = {'id':1230947608488636416}

retweet = twitter.post(END_POINT_URL)

print(retweet.status_code)
print(retweet["user"])