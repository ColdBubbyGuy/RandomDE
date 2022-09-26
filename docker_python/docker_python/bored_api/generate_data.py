import csv
import os
import requests

URL = "https://www.boredapi.com/api/activity"
CSV_FILE = "bored_ideas.csv"
KEY = "key"


def is_csv_empty():
    if os.stat(CSV_FILE).st_size == 0:
        return True
    return False


def create_headers(json_idea, csv_writer):
    header = json_idea.keys()
    csv_writer.writerow(header)


def generate_idea(ideas):
    bored_idea = requests.get(URL)
    json_idea = bored_idea.json()
    csv_file = open(CSV_FILE, 'a', newline='')
    csv_writer = csv.writer(csv_file)
    if is_csv_empty():
        create_headers(json_idea, csv_writer)
    exists = False
    for idea in ideas:
        if idea[KEY] == json_idea[KEY]:
            exists = True
            break
    if not exists:
        csv_writer.writerow(json_idea.values())
    csv_file.close()
    with open(CSV_FILE, mode="r") as csv_ideas:
        reader = csv.DictReader(csv_ideas)
        for idea in reader:
            if idea not in ideas:
                ideas.append(idea)
    csv_ideas.close()
