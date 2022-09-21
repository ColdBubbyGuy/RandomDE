from kafka.consumer import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    consumer.subscribe(['reddit_topic_one', 'reddit_topic_two'])

    for message in consumer:
        print(message.value)
