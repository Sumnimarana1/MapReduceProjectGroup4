from textblob import TextBlob
input = open("tweety.csv", "r")
positive_count = 0
negative_count = 0
neutral_count = 0
for i in input.readlines():
    result = TextBlob(i)
    #print(result.sentiment)
    if result.sentiment.polarity > 0:
        positive_count = positive_count + 1
    elif result.sentiment.polarity == 0:
        neutral_count = neutral_count + 1
    else:
        negative_count = negative_count + 1
print("Number of positive tweets ", positive_count)
print("Number of negative tweets ", negative_count)
print("Number of neutral tweets ", neutral_count)