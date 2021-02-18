import sys
import json
from typing import Collection
import pandas as pd
import tweepy
import os
import re
import itertools
import collections

class Tweets:
    def __init__(self,api):
        self.api = api


    #Returns a lsit of tweets that relate to the serch
    #Example: tweets = serch("#Playstation") or serch("Playstation") 
    #you can also serch for words that follow eachother serch("Playstation+5")
    def serch(self,criteria):
        return tweepy.Cursor(api.search,q=criteria,lang="en").items(5)


    #Same as serch but you can apply a filter to the tweets
    #serch("#Playstation","retweets")

    def serch_with_filter(self,criteria,filter):
        return tweepy.Cursor(api.search,q=criteria+" -filter:"+filter,lang="en").items(5)


    #Returns a lsit of tweets that relate to the serch an are after the specified date 
    #Example: tweets = serch_withDate("#Playstation","2020-11-16")

    def serch_withDate(self,criteria,date):
        return tweepy.Cursor(api.search,q=criteria,lang="en",since=date)


    #Returns a lsit of tweets that relate to the serch an are between the specified dates 
    #Example: tweets = serch_between_dates("#Playstation","2020-11-16","2020-12-16")

    def serch_between_dates(self,criteria,since,untill):
        return tweepy.Cursor(api.search,q=criteria,lang="en",since=since,untill=untill)



class Utils:
    def __init__(self) -> None:
        pass

        
    #Removes any urls from a tweet and replaces them with an empty string
    def remove_urls(tweet):
        return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())

    #returns a list of tweets with all the words split and the capitals removed 
    def split_and_remove_capitals(tweets):
        return [tweet.lower().split() for tweet in tweets]

    #returns a collection from a lsit of tweets 
    #EX:can be used to get the most common words with .most_common(15) returns the 15 most common words 
    def get_counter(tweets):
        all_words = list(itertools.chain(*tweets))
        return collections.Counter(all_words)

    #Removes common words that are not meaningful to analysis
    def remove_stop_words(tweets,stop_words):
        return [[word for word in tweet_words if not word in stop_words]
              for tweet_words in tweets]

    #Removes collections words from the tweets
    #collection words are the serch criteria used whe nserching for tweets 
    def remove_collection_words(tweets,collection_words):
        return [[w for w in word if not w in collection_words]
                  for word in tweets]


def get_api():
    with open(os.path.join(sys.path[0], "config.json"), "r") as file:
         keys = json.load(file)["KEYS"]
         
    auth = tweepy.OAuthHandler(keys["CONSUMER_KEY"], keys["CONSUMER_SECRET"])
    auth.set_access_token(keys["AccessToken"], keys["AccessTokenSecret"])

    return tweepy.API(auth)

#nltk.download('stopwords')
#stop_words = set(stopwords.words('english'))


api = get_api()

t = Tweets(api)


tweets = t.serch("Playstation")

tweets = [Utils.remove_urls(tweet.text) for tweet in tweets]

tweets = Utils.split_and_remove_capitals(tweets)

print(tweets)