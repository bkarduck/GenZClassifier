import pandas as pd
import numpy as np
import requests
import datetime as dt
import time
import os
import tqdm
import json
import praw # pip install praw, reddit API wrapper
#from psaw import PushshiftAPI # pip install psaw, pushshift.io API wrapper
from pmaw import PushshiftAPI # pip install pmaw, pushshift.io API wrapper
#from psaw import PushshiftAPI

# https://towardsdatascience.com/how-to-collect-a-reddit-dataset-c369de539114 

# for genz lingo: r/teenagers

# for adult lingo: r/RedditForGrownups



# to use PRAW you need to create a reddit app on reddit and insert your Client ID and Client Secret as well as your username and password for your reddit account and your user agent which is the name of the app you made for reddit

# If using this code, and you don't want to create a reddit app to alter the type of data you are collecting, you can use the data that I have already collected and stored in the json files. 

reddit = praw.Reddit(
    client_id = "",
    client_secret = "",
    username = "",
    password = "",
    user_agent = ""
)
api = PushshiftAPI()



subreddit = reddit.subreddit("teenagers")
teenDict = {}
for submission in reddit.subreddit("teenagers").search("flair:Discussion", limit=150, sort='top'):
    print(1)
 
    commentList = []
    
    submission.comments.replace_more(limit=0)
    count = 0
    for top_level_comment in submission.comments:
        commentList.append(top_level_comment.body)
        count += 1

        if count == 100:
            break

    teenDict[submission.id] = [submission.title, submission.selftext, commentList]
for submission in reddit.subreddit("teenagers").search("flair:Serious", limit=50, sort='top'):
    print(2)

    commentList = []
    
    submission.comments.replace_more(limit=0)
    count = 0
    for top_level_comment in submission.comments:
        commentList.append(top_level_comment.body)
        count += 1
 
        if count == 100:
            break

    teenDict[submission.id] = [submission.title, submission.selftext, commentList]
for submission in reddit.subreddit("teenagers").search("flair:Advice", limit=150, sort='top'):
    print(3)

    commentList = []
    
    submission.comments.replace_more(limit=0)
    count = 0
    for top_level_comment in submission.comments:
        commentList.append(top_level_comment.body)
        count += 1

        if count == 100:
            break
    teenDict[submission.id] = [submission.title, submission.selftext, commentList]

with open('teenDict.json', 'w') as fp:
    json.dump(teenDict, fp)

# reading the adult subreddit    

adultDict = {}
for submission in reddit.subreddit("RedditForGrownups").top(limit=300):
    print(4)
    commentList = []
    
    submission.comments.replace_more(limit=0)
    count = 0
    for top_level_comment in submission.comments:
        commentList.append(top_level_comment.body)
        count += 1
        if count == 100:
            break
    adultDict[submission.id] = [submission.title, submission.selftext, commentList]
with open('adultDict.json', 'w') as fp:
    json.dump(adultDict, fp)

