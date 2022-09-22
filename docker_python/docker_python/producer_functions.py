import json
from data_generator import generate_data
from kafka.producer import KafkaProducer

PRODUCE_FOR_TOPIC = "jokes_topic"


def react_to_joke(post):
    print("Do you want to react to this joke?")
    print("0 - Upvote")
    print("1 - Downvote")
    print("2 - Don't react")
    decision = input()
    if decision == "0":
        post.upvote()
        print("Successfully upvoted!")
    elif decision == "1":
        post.downvote()
        print("Successfully downvoted!")


def comment_on_joke(post):
    print("Do you want to write a comment?")
    print("0 - Yes")
    print("1 - No")
    decision = input()
    if decision == "0":
        print("Write your reply to the comment: ")
        comment = input()
        post.reply(comment)
        print("Successfully replied!")


def produce_jokes(subreddit, sort_criteria, number_of_the_joke):
    producer = create_producer()
    joke_info, post = generate_data(subreddit, sort_criteria, number_of_the_joke)
    partition_number = determine_partition(subreddit)
    producer.send(PRODUCE_FOR_TOPIC, joke_info, partition=partition_number)
    print(joke_info)
    react_to_joke(post)
    comment_on_joke(post)


def determine_partition(subreddit):
    if subreddit == "Jokes":
        return 0
    elif subreddit == "cleanjokes":
        return 1
    else:
        # DirtyJokes
        return 2


def create_producer():
    return KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=serializer)


def serializer(message):
    return json.dumps(message).encode('utf-8')
