import tweepy
import csv
####input your credentials here
consumer_key = 'cUl8PhvD2GBmBU7Oyu1yHcSzZ'
consumer_secret = 'KE2BoICmlSaNr75VWZtlXL5eIjLyRYR7hdBfVHwNAUd0P3PyFc'
access_token = '1008783848812023812-KkImFZ0o41ie8troJgwciwqLSSYfuw'
access_token_secret = 'qWoTlhuXronTzCdDdTmPOoLK0tr2oRHu9P3uoR0somtJk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=False)
# Open/Create a file to append data
csvFile = open('tweety.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
print('enter search string')
hashtag = input()
print(hashtag)
print('enter date')
date = input()
for tweet in tweepy.Cursor(api.search,q = hashtag,count = 9000, lang="en", since = date).items():
    print(tweet.text)
    csvWriter.writerow([str(tweet.text.encode('utf-8'))])
csvFile.close()