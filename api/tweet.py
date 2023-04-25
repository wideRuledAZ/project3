from cgi import print_directory
import tweepy
from api import generate_tweet

# Authenticate to Twitter API
api_key = "sPAcKr4jIrdbfO9NgLDbvc7kM"
api_secret = "hvUDOXDJ9in47PZJkIzNojCyytb3dK8PVNqrzQewwjUOijja0f"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAALTymgEAAAAA4WhfBd1XrguLaNk4gzO9y%2FSIHUw%3DuLdxxH3M3rr1ufHdDjjNoOdbdKSC36rpFsBA1uO8WSE3Cm3M8s"
access_token = "1647082491730354176-iz1toeqhUqkkKVxXgHh3hpzIC15qiP"
access_token_secret = "55zL62xZWvLngRLU5TWGTftrDjUn37EieSXF0nbzk14tg"

client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_token_secret)

# Example usage: post a tweet
userPrompt = "New York ->"

tweet = generate_tweet(userPrompt)

# tweet = "this is a tweet lol"
client.create_tweet(text=tweet)
print("Tweet posted:", tweet)