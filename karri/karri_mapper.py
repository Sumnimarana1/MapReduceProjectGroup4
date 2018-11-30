# Author - Krishna Veni Karri
# mapper code to collect live stream of tweets using Tweepy API and find sentiment of each tweet

import tweepy
from textblob import TextBlob

# input your twitter credentials here
consumer_key = '****'
consumer_secret = '***'
access_token = '*****-'
access_token_secret = '****'

# authenticate and set credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=False)

# Open/Create a file in append mode to store the retrieved tweets
mapper_output = open("tweety.txt", "a")

# take input from user: search word which is included in tweets or a hashtag and "from date"
print('enter search string')
hashtag = input()
print(hashtag)
print('enter date')
date = input()

# collect tweets, calculate sentiment for each tweet and write them to a text file
for tweet in tweepy.Cursor(api.search, q=hashtag, count=9000, lang="en", since=date).items():
    result = TextBlob(str(tweet.text))
    if result.sentiment.polarity > 0:
        mapper_output.write("{0},{1}\n".format("positive", str(tweet.text.encode('utf-8'))))
    elif result.sentiment.polarity == 0:
        mapper_output.write("{0},{1}\n".format("neutral", str(tweet.text.encode('utf-8'))))
    else:
        mapper_output.write("{0},{1}\n".format("negative", str(tweet.text.encode('utf-8'))))


print("SUCCESSFULLY COLLECTED TWEETS AND CALCULATED SENTIMENT!!\nPLEASE SEE THE RESULTS IN tweety.txt FILE.")
mapper_output.close()
