import json

def load_information(route):
  tweets = []
  file = open(route)

  for line in file:
    tweets.append(json.loads(line))

  return tweets

