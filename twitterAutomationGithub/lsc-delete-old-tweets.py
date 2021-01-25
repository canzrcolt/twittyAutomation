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
start_id = 1191423930839363584       
end_id = 1189233573456465921

i = 1
for status in tweepy.Cursor(api.user_timeline).items():
    if (status.id <= start_id and status.id >= end_id) and status.id != 700808989886382080:
        print(status.id, i)
        api.destroy_status(status.id)
        i += 1
    elif status.id == 700808989886382080:
        print ('zzzzzzzzzzzzzzzzz')


   

# public_All_tweets = api.home_timeline(count = 12000)
# for tweets in public_All_tweets:
#     tweet_date = tweets.created_at
#     print(tweets.created_at) 
        
# with open('tweet.json') as json_file:
#     my_data = json.load(json_file)
#START_DATE = datetime(1970, 1, 1, 0, 0, 0)
#END_DATE = datetime(2017, 10, 20, 0, 0, 0)




















# days_to_keep = 365
# cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_to_keep)
# print(cutoff_date)


# file_pointer = open("tweet.js","r")

# my_json = json.loads(file_pointer)


#test_id = '688010300969336832'

#public_tweet = api.get_status(test_id)
























#destroy_tweet = api.destroy_status(test_id)

#cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days = 365)
#print(cutoff_date)


#public_All_tweets = api.home_timeline(count = 10)

#for tweets in public_All_tweets:

   # print(tweets.id)
    
