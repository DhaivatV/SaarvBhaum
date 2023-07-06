import tweepy
from dotenv import load_dotenv
from dotenv import dotenv_values
from main import generate_tweet
import time
import datetime

def give_time():
    now = datetime.datetime.now()
    return (now.strftime("%Y-%m-%d %H:%M:%S"))

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
            with open("logs.txt", "a+", encoding='utf-8') as f:
                f.seek(0)  # Move the file pointer to the beginning
                data = f.read()
                f.write(f"\ntweet sent, {give_time()}")
            time.sleep(1800)
        except Exception as e:
            with open("logs.txt", "a+", encoding='utf-8') as f:
                f.seek(0)  # Move the file pointer to the beginning
                data = f.read()
                f.write("\n"+str(e)+f"{give_time()}")
            print("Error, trying again")

