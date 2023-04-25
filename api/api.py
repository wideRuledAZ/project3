from purgo_malum import client
from time import time
from flask import Flask, jsonify
import os
import openai
import json
from cgi import print_directory
import tweepy

# Authenticate to Twitter API
api_key = "sPAcKr4jIrdbfO9NgLDbvc7kM"
api_secret = "hvUDOXDJ9in47PZJkIzNojCyytb3dK8PVNqrzQewwjUOijja0f"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAALTymgEAAAAA4WhfBd1XrguLaNk4gzO9y%2FSIHUw%3DuLdxxH3M3rr1ufHdDjjNoOdbdKSC36rpFsBA1uO8WSE3Cm3M8s"
access_token = "1647082491730354176-iz1toeqhUqkkKVxXgHh3hpzIC15qiP"
access_token_secret = "55zL62xZWvLngRLU5TWGTftrDjUn37EieSXF0nbzk14tg"

twClient = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_token_secret)

app = Flask(__name__)

# Initialize the OpenAI library
openai.api_key = "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"

# Creating a route for generating a tweet, where userPrompt is a string parameter that represents the user's prompt for the tweet.
# Contributions: Daniel Martinez and ChatGPT
@app.route('/generate_tweet/<string:userPrompt>')
def generate_tweet(userPrompt):
    if (userPrompt == None):
        return ''
    print("asking bot")
    # Generate a prompt for GPT-3 to complete
    print("getting tweet")
    
    while True:
        # Send the API request to GPT-3
        response = openai.Completion.create(
                model="davinci:ft-personal-2023-04-24-02-14-12",
                prompt=userPrompt,
                temperature=0.8,
                max_tokens = 300
        )
    
        # Get the generated tweet from the API response
        generated_text = response.choices[0].text.strip()
        
        # Check if generated text contains any of the avoid words
        if (not client.contains_profanity(generated_text, add='abuse, profanity, hate speech, sex, racism')):
            tweets = generated_text.split("\n")
            tweet = tweets[0] # get the first tweet of the options
            return json.dumps(tweet)

# Creating a route for posting a tweet, where tweet is a string parameter that represents the text of the tweet.
# Contributions: Daniel Martinez and ChatGPT
@app.route('/post_tweet/<string:tweet>')
def post_tweet(tweet):
    twClient.create_tweet(text=tweet)
    return json.dumps("Tweet posted")

if __name__ == '__main__':
    app.run(debug=True)