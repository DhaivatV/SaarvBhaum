import urllib.request
import fitz
import re
import numpy as np
import openai
import os
from dotenv import load_dotenv
from dotenv import dotenv_values
import pandas as pd
import random

load_dotenv()
config = dotenv_values(".env")

openai.api_key = config['openai_api_key']

def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number

def generate_text(prompt, engine="text-davinci-003"):
    completions = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message


def generate_answer(topn_chunks):

    prompt = ""
    prompt += 'Book Data:\n\n'
    for c in topn_chunks:
        prompt += c + '\n\n'

    prompt += "Unveil the hidden layers of wisdom within the provided book data and create one captivating tweets within a word limit of 240 characters with proper hashtags that will capture the attention of millions."\
              "Craft thought-provoking messages, intriguing quotes, or fascinating facts derived from the data to ignite discussions and engage a wide audience on social media."\
              "Unleash your creativity and transform the book's knowledge into viral tweets that leave a lasting impact on readers worldwide.\n\n"\
              "Very Important Instructions : \n"\
              "1. Pleae make sure not cite each reference using [number] notation (every result has this number at the beginning).\n"\
              "2. Stick to the character limit of 240 characters.\n"\
              "3. Don't start the response with 'tweet:' or 'Tweet'.\n"\
              "4. Dont mention name J. Sai Deepak in the tweet.\n"\
              "5. Don't add any additional information answer from the book data provided. Make sure the answer is correct and don't output false content.\n"\
              "6. In the tweet dont mention the source of the information.\n"
              


    prompt += f"follow the instructions generate an appropriate response\n\n"
    answer = generate_text(prompt)

    if type(answer)==list:
        return(answer[0])
    else:
        return answer

def main(content_chunks_list):

    topn_chunks = content_chunks_list
    res = generate_answer(topn_chunks)
    return res


def generate_tweet():

    df= pd.read_csv('chunk-content.csv')
    content_list = df['content'].to_list()
    idx_val = generate_random_number(0, len(content_list)-5)

    content_data_list = []

    for i in range(idx_val, idx_val+5):
        content_data_list.append(content_list[i])
    
    tweet = main(content_data_list)

    return tweet

