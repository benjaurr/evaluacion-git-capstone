import json
from operator import itemgetter

def load_information(route):
  tweets = []
  file = open(route)

  for line in file:
    tweets.append(json.loads(line))

  return tweets

def most_retweeted(tweets):
  sorted_tweets = sorted(tweets, key=itemgetter('retweetCount'), reverse=True)
  return sorted_tweets[0:10]