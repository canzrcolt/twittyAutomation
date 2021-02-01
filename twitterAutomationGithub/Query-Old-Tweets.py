import tweepy
import datetime, json, os, time
from os import path, stat
from datetime import timezone, datetime, timedelta

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



myData = []
with open('listOfIDs.txt', 'r') as text_file:
    data = text_file.readlines()
    
    for not_formatted_ids in data:
        myData += not_formatted_ids.strip().split(", ")
    for tweetIDs in myData:
        try:
            
            print(api.get_status(tweetIDs).id)
        except:
            print('didnt exist')
