import tweepy
from dotenv import load_dotenv
from dotenv import dotenv_values
from main import generate_tweet
import time

load_dotenv()
config = dotenv_values(".env")

client = tweepy.Client(consumer_key= config['consumer_key'],
                       consumer_secret= config['consumer_secret'],
                       access_token= config['access_token'],
                       access_token_secret= config['access_token_secret'])



def create_tweet(tweet):
    response = client.create_tweet(text=tweet)
    return response

if __name__ == "__main__":

    while True:
        tweet = generate_tweet()
        try:
            create_tweet(tweet)
            print("tweet created")
            time.sleep(1800)
        except Exception as e:
            print("Error, trying again")

