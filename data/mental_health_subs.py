#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import praw
import json
from tqdm import tqdm


subreddit_list = ['mentalhealth',
                  'depression',
                  'Anxiety',
                  'bipolar',
                  'BPD',
                  'SuicideWatch',
                  'CasualConversation']

data_dictionary = {
    'title': [],
    'body': [],
    'author': [],
    'url': [],
    'score': [],
    'upvote_ratio': [],
    'subreddit': []
}

with open("reddit_credentials.json") as f:
    credentials = json.load(f)

reddit_api = praw.Reddit(client_id=credentials['client_id'],
                         client_secret=credentials['client_secret'],
                         user_agent=credentials['user_agent'])

for subreddit in tqdm(subreddit_list):

    limit = 1000

    if subreddit == 'CasualConversation':
        limit = 6000

    for post in tqdm(reddit_api.subreddit(subreddit).hot(limit=limit)):

        data_dictionary['title'].append(post.title)
        data_dictionary['body'].append(post.selftext)
        data_dictionary['author'].append(post.author)
        data_dictionary['url'].append(post.url)
        data_dictionary['score'].append(post.score)
        data_dictionary['upvote_ratio'].append(post.upvote_ratio)
        data_dictionary['subreddit'].append(subreddit)

mental_health_data = pd.DataFrame.from_dict(data_dictionary)
mental_health_data.to_csv('mental_health_data.csv')




