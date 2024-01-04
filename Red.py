'''
Reddit Reply Bot
-------------------------------------------------------------
pip install praw pyenchant
'''

import praw
import enchant

def reddit_bot(sub, trigger_phrase):
    reddit = praw.Reddit(
        client_id = 'your_client_id',
        client_secret = 'your_client_secret',
        username = 'your_username',
        password = 'your_pw',
        user_agent = 'your_user_agent'
    )