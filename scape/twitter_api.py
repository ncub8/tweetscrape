import twitter
import os
import json

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
OAUTH_SECRET = os.environ.get('OAUTH_SECRET')

US_WOE_ID = 23424977

twitter_api = twitter.Twitter(auth=twitter.OAuth(str(OAUTH_TOKEN), str(OAUTH_SECRET), str(CONSUMER_KEY), str(CONSUMER_SECRET)), retry=True)



def get_trending():
    trends = twitter_api.trends.place(_id=US_WOE_ID)
    us_trends = trends[0]['trends']
    return us_trends

def get_popular(term):
    popular = twitter_api.search.tweets(q=term, count=100, result_type="popular")
    return popular

