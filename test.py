import pandas as pd 

df = pd.read_csv('sent_tweets.csv')

dict_con = {

    'SentTweets':'abcd',
    'idxval':0
}

df = pd.concat([df, pd.DataFrame([dict_con])], ignore_index=True)
df.to_csv('sent_tweets.csv',index=False)

