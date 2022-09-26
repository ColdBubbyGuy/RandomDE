import json
import random
import copy

from kafka import KafkaProducer

from helper_functions import *
from enum import Enum

CRITERIA_TYPE = "type"
CRITERIA_PARTICIPANTS = "participants"
CRITERIA_PRICE = "price"
CRITERIA_ACCESSIBILITY = "accessibility"

TITLE_TYPE = "Number of ideas by type"
TITLE_PRICE = "Number of ideas by price"
TITLE_ACCESSIBILITY = "Number of ideas by accessibility"

NUM_OF_IDEAS_STR = "Number of ideas"

TOPIC = 'bored'


class Operator(Enum):
    Equals = 1,
    NotEquals = 2,
    Less = 3,
    LessEquals = 4
    More = 5,
    MoreEquals = 6


def send_message(producer, message):
    producer.send(TOPIC, message)


def serializer(message):
    return json.dumps(message).encode('utf-8')


def create_producer():
    return KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=serializer)


def find_operator(starting_char, ending_char):
    if starting_char == "=" and ending_char == "=":
        return Operator.Equals
    elif starting_char == "!" and ending_char == "=":
        return Operator.NotEquals
    elif starting_char == "<" and ending_char != "=":
        return Operator.Less
    elif starting_char == "<" and ending_char == "=":
        return Operator.LessEquals
    elif starting_char == ">" and ending_char != "=":
        return Operator.More
    elif starting_char == ">" and ending_char == "=":
        return Operator.MoreEquals


def search_by_criteria(type_criteria, participants_criteria, price_criteria, accessibility_criteria, ideas_copy,
                       producer):
    ideas_copy = search_by_type(type_criteria, ideas_copy)
    ideas_copy = search_by_participants(participants_criteria, ideas_copy)
    ideas_copy = search_by_price(price_criteria, ideas_copy)
    ideas_copy = search_by_accessibility(accessibility_criteria, ideas_copy)
    for idea in ideas_copy:
        idea = dictionary_to_output(idea)
        send_message(producer, idea)


def extract_type_criteria(type_criteria):
    criteria_parts = type_criteria.split("==")
    return criteria_parts[1]


def search_general(operator, criteria, ideas_copy, criteria_name):
    if operator == operator.Equals:
        return [idea for idea in ideas_copy if float(idea[criteria_name]) == float(criteria)]
    elif operator == operator.NotEquals:
        return [idea for idea in ideas_copy if float(idea[criteria_name]) != float(criteria)]
    elif operator == operator.Less:
        return [idea for idea in ideas_copy if float(idea[criteria_name]) < float(criteria)]
    elif operator == operator.LessEquals:
        return [idea for idea in ideas_copy if float(idea[criteria_name]) <= float(criteria)]
    elif operator == operator.More:
        return [idea for idea in ideas_copy if float(idea[criteria_name]) > float(criteria)]
    # MoreEquals
    else:
        return [idea for idea in ideas_copy if float(idea[criteria_name]) >= float(criteria)]


def extracted_criteria_general(criteria, operator, starting_index):
    if operator == Operator.More or operator == Operator.Less:
        return criteria[starting_index:]
    return criteria[starting_index + 1:]


def search_by_type(type_criteria, ideas_copy):
    extracted_criteria = extract_type_criteria(type_criteria)
    return [idea for idea in ideas_copy if idea[CRITERIA_TYPE] == extracted_criteria]


def search_by_participants(participants_criteria, ideas_copy):
    operator = find_operator(participants_criteria[12], participants_criteria[13])
    extracted_criteria = extracted_criteria_general(participants_criteria, operator, 13)
    return search_general(operator, extracted_criteria, ideas_copy, CRITERIA_PARTICIPANTS)


def search_by_price(price_criteria, ideas_copy):
    operator = find_operator(price_criteria[5], price_criteria[6])
    extracted_criteria = extracted_criteria_general(price_criteria, operator, 6)
    return search_general(operator, extracted_criteria, ideas_copy, CRITERIA_PRICE)


def search_by_accessibility(accessibility_criteria, ideas_copy):
    operator = find_operator(accessibility_criteria[13], accessibility_criteria[14])
    extracted_criteria = extracted_criteria_general(accessibility_criteria, operator, 14)
    return search_general(operator, extracted_criteria, ideas_copy, CRITERIA_ACCESSIBILITY)


def generate_a_random_idea(ideas, producer):
    idea = dictionary_to_output(random.choice(ideas))
    send_message(producer, idea)


def generate_ideas_based_on_criteria(criteria, ideas, producer):
    ideas_copy = copy.deepcopy(ideas)
    type_criteria, participants_criteria, price_criteria, accessibility_criteria = criteria.split(' ')
    search_by_criteria(type_criteria, participants_criteria, price_criteria, accessibility_criteria, ideas_copy,
                       producer)


def generate_graph_by_idea_types(ideas, producer):
    ideas_types_dictionary = {"education": 0, "recreational": 0, "social": 0, "diy": 0, "charity": 0, "cooking": 0,
                              "relaxation": 0, "music": 0, "busywork": 0}
    for idea in ideas:
        ideas_types_dictionary[idea[CRITERIA_TYPE]] += 1
    plot_key_graph(ideas_types_dictionary, TITLE_TYPE, CRITERIA_TYPE, NUM_OF_IDEAS_STR)
    send_message(producer, ideas_types_dictionary)


def generate_graph_by_idea_prices_or_accessibility(ideas, producer, criteria):
    ideas_dictionary = {}
    for idea in ideas:
        if idea[criteria] not in ideas_dictionary.keys():
            ideas_dictionary[idea[criteria]] = 0
        ideas_dictionary[idea[criteria]] += 1
    ideas_dictionary = dict(sorted(ideas_dictionary.items()))
    if criteria == CRITERIA_PRICE:
        plot_key_graph(ideas_dictionary, TITLE_PRICE, CRITERIA_PRICE, NUM_OF_IDEAS_STR)
    elif criteria == CRITERIA_ACCESSIBILITY:
        plot_key_graph(ideas_dictionary, TITLE_ACCESSIBILITY, CRITERIA_ACCESSIBILITY, NUM_OF_IDEAS_STR)
    send_message(producer, ideas_dictionary)
