import json
import urllib2

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#twitter information
access_token = '2485664815-EZZNyloRAwylWUHaPfmDDt6OufJHbYsoDB9dAwp'
access_token_secret = 'nDtAqPEYwZC6jhRU8c5L24QXvbQSJEjqeFoejuHNf0lF8'
consumer_key = 'l5YODKJF8HGZc0rE7kYNo9C6t'
consumer_secret = 'rM2wU2ups2XLyV4I1jJTcoOa3KYFpUowE49OJcHfYhHQxHiYiC'

class tweet_listener(StreamListener):
    def on_data(self, raw_data):
        tweet_text = json.loads(raw_data)
        print(tweet_text['text'])
        return True

#get the tweets
def get_tweets():
    l = tweet_listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    stream.filter(track =['AI'], languages=['en'])

get_tweets()