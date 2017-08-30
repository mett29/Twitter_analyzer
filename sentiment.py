import tweepy
from textblob import TextBlob

# Import twitter keys and tokens
from config import *

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

# Retrieve Tweets
public_tweets = api.search('trump')

for tweet in public_tweets:
    print(tweet.text)
    
    # Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    # Determine if sentiment is positive, negative, or neutral
    if analysis.sentiment.polarity < 0:
        sentiment = "negative"
    elif analysis.sentiment.polarity == 0:
        sentiment = "neutral"
    else:
        sentiment = "positive"

    # Output sentiment
    print(sentiment)
    print("")


