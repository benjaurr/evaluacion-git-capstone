import json
from operator import itemgetter
from collections import defaultdict
from datetime import datetime, date

def load_information(route):
  tweets = []
  file = open(route)

  for line in file:
    tweets.append(json.loads(line))

  return tweets

def most_retweeted(tweets):
  sorted_tweets = sorted(tweets, key=itemgetter('retweetCount'), reverse=True)
  return sorted_tweets[0:10]

def most_emited_tweets(tweets):
  user_tweet_count = defaultdict(lambda: 0)

  for tweet in tweets:
    user_tweet_count[tweet['user']['username']] += 1

  top_users = sorted(user_tweet_count, key=user_tweet_count.get, reverse=True)[:10]
  return { k: user_tweet_count[k] for k in top_users }

def top_ten_tweeted_days(tweets):
  date_tweet_count = defaultdict(lambda: 0)

  for tweet in tweets:
    date_tweet_count[tweet['date'][:10]] += 1

  top_dates = sorted(date_tweet_count, key=date_tweet_count.get, reverse=True)[:10]
  return { k: date_tweet_count[k] for k in top_dates }