import praw
import datetime

reddit = praw.Reddit(client_id='63mLLMBEhIAd2fKmw-LxFA',
                     client_secret='LGMrgAxwoJRLX68S6rZ9UKIVLDYwDg',
                     username='ColdBubbyGuy',
                     password='AllenTolicki166',
                     user_agent='myUserAgent')

for submission in reddit.subreddit("askReddit").top(limit=25):
    print("Title: " + submission.title)
    print("Date created: " + str(datetime.datetime.fromtimestamp(submission.created_utc)))
    for comment in submission.comments:
        print("Top comment: " + comment.body)
        print("Number of upvotes: " + str(comment.score))
        break
    print(30*'=')
