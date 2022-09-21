import praw
import random
import datetime

# https://www.youtube.com/watch?v=LHNtL4zDBuk&ab_channel=BetterDataScience  useful kafka tutorial
# https://www.conduktor.io/kafka/kafka-topics-cli-tutorial#How-to-list-Kafka-Topics?-1 working with kafka commands in command line

REDDIT = praw.Reddit(client_id='63mLLMBEhIAd2fKmw-LxFA',
                     client_secret='LGMrgAxwoJRLX68S6rZ9UKIVLDYwDg',
                     username='ColdBubbyGuy',
                     password='AllenTolicki166',
                     user_agent='myUserAgent')


def generate_data(subredit_name):
    subreddit = REDDIT.subreddit(subredit_name)
    posts = [post for post in subreddit.hot(limit=100)]
    random_post_number = random.randint(0, 99)
    random_post = posts[random_post_number]

    title = random_post.title
    post_score = random_post.score
    date_created = str(datetime.datetime.fromtimestamp(random_post.created_utc))
    top_comment = random_post.comments[0].body
    top_comment_score = random_post.comments[0].score

    return {
        "Title": title,
        "Post score": post_score,
        "Date of post creation": date_created,
        "Top comment": top_comment,
        "Top comment score": top_comment_score,
        "Subreddit": subredit_name
    }

# jokes, facts, ...
# how many?
# sort by - ?
