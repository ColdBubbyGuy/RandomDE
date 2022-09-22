from kafka.consumer import KafkaConsumer
from kafka.structs import TopicPartition

CONSUME_FROM_TOPIC = "jokes_topic"


def create_consumer(partition):
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest', group_id=0)
    consumer.assign([TopicPartition(CONSUME_FROM_TOPIC, partition)])
    return consumer


def print_jokes(consumer):
    for joke in consumer:
        print(joke.value)
