import twitter
import os
import json
from collections import Counter
from alchemyapi import AlchemyAPI



CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
OAUTH_SECRET = os.environ.get('OAUTH_SECRET')

US_WOE_ID = 23424977

twitter_api = twitter.Twitter(auth=twitter.OAuth(str(OAUTH_TOKEN), str(OAUTH_SECRET), str(CONSUMER_KEY), str(CONSUMER_SECRET)), retry=True)

alchemyapi = AlchemyAPI()

def get_trending():
    trends = twitter_api.trends.place(_id=US_WOE_ID)
    us_trends = trends[0]['trends']
    return us_trends


def get_popular(term):
    """ Searches for tweets for a given term """
    popular = twitter_api.search.tweets(q=term, count=100, result_type="popular")
    statuses = popular['statuses']
    
    #just a list of the tweets
    texts = [status['text'] for status in statuses]
    
    #get the most common words
    popular['most_common'] = get_common(texts)
    
    #join the tweets into a text string and analyze
    text = ". ".join(texts)
    popular['sentiment'] = get_sentiment(text)
    
    return popular


def get_common(texts):
    """ Analyzes the most common words in tweets """
    #statuses = tweets['statuses']
    #texts = [status['text'] for status in statuses]
    #split the texts into words
    words = [w for t in texts for w in t.split()]
    common = []
    for item in[words]:
        c = Counter(item)
        common = c.most_common()[:25] #top 25
    return common

def get_sentiment(text):
    """ Uses the Alchemy API to do a keyword sentiment analysys of combined tweets """
    response = alchemyapi.keywords('text', text, {'sentiment': 1})
    
    return response