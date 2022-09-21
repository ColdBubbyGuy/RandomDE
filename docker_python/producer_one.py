import time
import json
import random
from datetime import datetime
from data_generator import generate_data
from kafka.producer import KafkaProducer

SUBREDDIT_ONE = "todayilearned"


def serializer(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        dummy_message = generate_data(SUBREDDIT_ONE)
        print(f"Producing message @ {datetime.now()} | Message = {str(dummy_message)}")
        producer.send('reddit_topic_one', dummy_message)

        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)
