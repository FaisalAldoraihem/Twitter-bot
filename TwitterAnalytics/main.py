import sys
import json
import pandas
import tweepy
import os

def GetApi():
    with open(os.path.join(sys.path[0], "config.json"), "r") as file:
         keys = json.load(file)["KEYS"];
         
    auth = tweepy.OAuthHandler(keys["CONSUMER_KEY"], keys["CONSUMER_SECRET"])
    auth.set_access_token(keys["AccessToken"], keys["AccessTokenSecret"])

    return tweepy.API(auth)
                      

   
api = GetApi()

# api.update_status("Twitter bot 2.0 Test Test ")

def serch_hashtag_withDate(hashtag,date):
    return tweepy.Cursor(api.search,q=hashtag,lang="en",since=date).items(5)


tweets = serch_hashtag_withDate("#Splatoon","2018-11-16")

for tweet in tweets:
    print(tweet.text)


