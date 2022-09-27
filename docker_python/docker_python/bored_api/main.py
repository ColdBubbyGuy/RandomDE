from generate_data import *
from producer import *

CSV_FILE = "bored_ideas.csv"
ideas = []


def load_data():
    with open(CSV_FILE, mode="r") as csv_ideas:
        reader = csv.DictReader(csv_ideas)

        for idea in reader:
            ideas.append(idea)

    csv_ideas.close()


def generate_ideas(additional_ideas):
    for i in range(int(additional_ideas)):
        generate_idea(ideas)
        if i % 50 == 0 and i != 0:
            print(str(i), " ideas loaded...")


def calculate_number_of_rows():
    return len(ideas)


if __name__ == "__main__":
    print("===========")
    print("BORED IDEAS")
    print("===========")
    print("Loading data...")
    load_data()
    producer = create_producer()
    number_of_ideas = calculate_number_of_rows()
    print("Number of existing ideas:", str(number_of_ideas))
    print("How many do you want to add?")
    additional_rows = input()
    if int(additional_rows) > 0:
        generate_ideas(additional_rows)
        print("Successfully added " + additional_rows + " rows!")
    while True:
        print("Functionalities:")
        print("1 - generate a random idea")
        print("2 - generate ideas based on criteria")
        print("3 - graphical data visualization")
        functionality = input()
        if functionality == "1":
            generate_a_random_idea(ideas, producer)
        elif functionality == "2":
            print("Input should be:")
            print("type==type_input participants*participants_input price*price_input accessibility*accessibility_input")
            print("* represents ==, <, >, <= , >=, != operators")
            print("type_input possible entries: education, recreational, social, "
                  "diy, charity, cooking, relaxation, music, busywork")
            print("participants_input possible entries: a number between 0 and n")
            print("price_input possible entries: a number between 0 and 1")
            print("accessibility_input possible entries: a number between 0 and 1")
            criteria = input()
            generate_ideas_based_on_criteria(criteria, ideas, producer)
        elif functionality == "3":
            print("Graphs: ")
            print("1 - ideas grouped by type")
            print("2 - ideas grouped by price")
            print("3 - ideas grouped by accessibility")
            print("4 - the least/most expensive idea sorted by type")
            graph_choice = input()
            if graph_choice == "1":
                generate_graph_by_idea_types(ideas, producer)
            elif graph_choice == "2":
                generate_graph_by_idea_prices_or_accessibility(ideas, producer, "price")
            elif graph_choice == "3":
                generate_graph_by_idea_prices_or_accessibility(ideas, producer, "accessibility")
            elif graph_choice == "4":
                generate_price_extremes_graph(ideas, producer)
        print("Do you want to use another function?")
        print("Y/n")
        decision = input()
        if decision == "n":
            exit(1)
