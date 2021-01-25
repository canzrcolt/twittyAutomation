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

year_ago = 1218289755240091648

i = 1
for status in tweepy.Cursor(api.user_timeline).items():
    if status.id < year_ago and status.id != 700808989886382080:
        print(status.id, i)
        
        i += 1
    elif status.id == 700808989886382080:
        print ('zzzzzzzzzzzzzzzzz')
