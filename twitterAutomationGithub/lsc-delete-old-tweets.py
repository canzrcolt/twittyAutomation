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

# year_ago = 1218289755240091648

# i = 1
# for status in tweepy.Cursor(api.user_timeline).items():
#     if status.id < year_ago and status.id != 700808989886382080:
#         print(status.id, i)
        
#         i += 1
#     elif status.id == 700808989886382080:
#         print ('zzzzzzzzzzzzzzzzz')
# test_id = 690635759586545664
# api.get_status(test_id)

myData = []
with open('listOfIDs.txt', 'r') as text_file:
    data = text_file.readlines()
    
    for not_formatted_ids in data:
        myData += not_formatted_ids.strip().split(", ")
    for tweetIDs in myData:
        try:
            print(api.destroy_status(tweetIDs).id)
        except:
            print('didnt exist')

    