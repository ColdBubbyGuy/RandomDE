from kafka import KafkaConsumer

TOPIC = 'bored'


def create_consumer():
    idea_consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    idea_consumer.subscribe([TOPIC])
    return idea_consumer


def print_jokes(idea_consumer):
    for idea in idea_consumer:
        print(idea.value)


if __name__ == "__main__":
    consumer = create_consumer()
    print_jokes(consumer)
