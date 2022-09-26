import praw
import datetime

# https://www.youtube.com/watch?v=LHNtL4zDBuk&ab_channel=BetterDataScience  useful kafka tutorial
# https://www.conduktor.io/kafka/kafka-topics-cli-tutorial#How-to-list-Kafka-Topics?-1 working with kafka commands in
# command line

# docker exec -it kafka /bin/sh

REDDIT = praw.Reddit(client_id='63mLLMBEhIAd2fKmw-LxFA',
                     client_secret='LGMrgAxwoJRLX68S6rZ9UKIVLDYwDg',
                     username='ColdBubbyGuy',
                     password='AllenTolicki166',
                     user_agent='myUserAgent')


def get_posts(sort_criteria, subreddit, number_of_the_joke):
    posts = []
    if sort_criteria == "0":
        posts = [post for post in subreddit.hot(limit=int(number_of_the_joke) + 1)]
    elif sort_criteria == "1":
        posts = [post for post in subreddit.top(limit=int(number_of_the_joke) + 1)]
    elif sort_criteria == "2":
        posts = [post for post in subreddit.new(limit=int(number_of_the_joke) + 1)]
    elif sort_criteria == "3":
        posts = [post for post in subreddit.rising(limit=int(number_of_the_joke) + 1)]
    return posts[-1]


def generate_for_consumer(chosen_post):
    title = chosen_post.title
    post_body = chosen_post.selftext
    post_score = chosen_post.score
    date_created = str(datetime.datetime.fromtimestamp(chosen_post.created_utc))
    top_comment = ""
    top_comment_score = ""
    if chosen_post.comments:
        top_comment = chosen_post.comments[0].body
        top_comment_score = chosen_post.comments[0].score
    return title, post_body, post_score, date_created, top_comment, top_comment_score


def generate_data(subreddit_name, sort_criteria, number_of_the_joke):
    subreddit = REDDIT.subreddit(subreddit_name)
    print("Loading...")
    chosen_post = get_posts(sort_criteria, subreddit, number_of_the_joke)
    title, post_body, post_score, date_created, top_comment, top_comment_score = generate_for_consumer(chosen_post)

    return {
        "Title": title,
        "Post body": post_body,
        "Post score": post_score,
        "Date of post creation": date_created,
        "Top comment": top_comment,
        "Top comment score": top_comment_score,
        "Subreddit": subreddit_name
    }, chosen_post
