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

def top_ten_used_hashtags(tweets):
  hashtage_tweet_count = defaultdict(lambda: 0)

  for tweet in tweets:
    hashtags = filter(lambda t: t[0] == '#', tweet['content'].split())
    for hashtag in hashtags:
      hashtage_tweet_count[hashtag] += 1

  top_hashtags = sorted(hashtage_tweet_count, key=hashtage_tweet_count.get, reverse=True)[:10]
  return { k: hashtage_tweet_count[k] for k in top_hashtags }

def main(): # as an example, all functions are used
  tweets = load_information("evaluacion-git-capstone/farmers-protest-tweets-2021-03-5.json") # make sure route is correct
  print(most_retweeted(tweets))
  print(most_emited_tweets(tweets))
  print(top_ten_tweeted_days(tweets))
  print(top_ten_used_hashtags(tweets))

main()