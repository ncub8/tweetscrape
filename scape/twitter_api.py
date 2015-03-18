import twitter
import os
import json
from collections import Counter



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
    """ Searches for tweets for a given term """
    popular = twitter_api.search.tweets(q=term, count=100, result_type="recent")
    popular['most_common'] = get_common(popular)
    return popular


def get_common(tweets):
    """ Analyzes the most common words in tweets """
    statuses = tweets['statuses']
    texts = [status['text'] for status in statuses]
    words = [w for t in texts for w in t.split()]
    common = []
    for item in[words]:
        c = Counter(item)
        common = c.most_common()[:25] #top 25
    return common