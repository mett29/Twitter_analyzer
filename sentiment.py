import tweepy
import time
from textblob import TextBlob

# Import twitter keys and tokens
from config import *

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

keyword = input("Insert the keyword: ")

def analyze(keyword): 

    # Initialize variables to calculate the average sentiment
    polaritySum = 0
    counter = 0

    # Retrieve Tweets
    public_tweets = api.search(keyword)

    for tweet in public_tweets:
        #print(tweet.text)
        
        # Perform Sentiment Analysis on Tweets
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        polaritySum += analysis.sentiment.polarity
        counter += 1
        # Determine if sentiment is positive, negative, or neutral
        if analysis.sentiment.polarity < 0:
            sentiment = "negative"
        elif analysis.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # Output sentiment
        #print(sentiment + '\n')

        return polaritySum/counter

while(True):
    average = analyze(keyword)
    print("The average sentiment's polarity is " + str(average))
    time.sleep(1800) # 30 mins