#Author - Krishna Veni Karri
#mapper code to collect live stream of tweets using Tweepy API and store them in a CSV File

import tweepy
import csv
####input your twitter credentials here
consumer_key = '*******************'
consumer_secret = '**********'
access_token = '********************'
access_token_secret = '*******************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=False)

# Open/Create a file in append mode
csvFile = open('tweety.csv', 'a')

#Use csv Writer to write tweets to a file
csvWriter = csv.writer(csvFile)
#take input from user: search word which is included in tweets and from date
print('enter search string')
hashtag = input()
print(hashtag)
print('enter date')
date = input()

#collect tweets and write them to csv
for tweet in tweepy.Cursor(api.search,q = hashtag,count = 9000, lang="en", since = date).items():
    print(tweet.text)
    csvWriter.writerow([str(tweet.text.encode('utf-8'))])
csvFile.close()