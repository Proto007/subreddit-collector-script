"""
This script allows users to collect specified number of hot reddit posts from the specified subreddit.

CLI argument 1: name of subreddit
CLI argument 2: number of hot posts

Output: CSV file with the name of the provided subreddit

Example Usage:  `python subreddit_collector.py python 100`
This will output a CSV file named `python.csv` containing 100 hot posts from the python subreddit
"""

import os
import sys

import pandas as pd
import praw
from dotenv import load_dotenv

# Load the environment variables and initialize praw with the proper credentials
load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent="subreddit_collector_v1",
)

# Get the specified number of posts for the specified subreddit
subreddit = reddit.subreddit(sys.argv[1])
hottest_info = subreddit.hot(limit=int(sys.argv[2]))

# Iterate through the submissions and collect the appropriate information
titles, authors, ratios, upvotes, comments, times = [], [], [], [], [], []
for submission in hottest_info:
    if not submission.stickied:
        titles.append(submission.title)
        authors.append(submission.author)
        ratios.append(submission.upvote_ratio)
        upvotes.append(submission.ups)
        comments.append(submission.num_comments)
        times.append(submission.created_utc)

# Create a dataframe with the collected info
df = pd.DataFrame(
    {
        "Title": titles,
        "Author": authors,
        "Upvote Ratio": ratios,
        "Upvotes": upvotes,
        "Comments": comments,
        "Time": times,
    }
)

# Save the dataframe as a .csv file
df.to_csv(f"{sys.argv[1]}.csv")

print(
    f"`{sys.argv[1]}.csv` created successfully with {sys.argv[2]} posts from the {sys.argv[1]} subreddit !!!"
)
