from producer_functions import produce_jokes

JOKES_SUBREDDIT = "Jokes"
DIRTY_JOKES_SUBREDDIT = "DirtyJokes"
ClEAN_JOKES_SUBREDDIT = "cleanjokes"


def find_subreddit(type_of_joke):
    if type_of_joke == "0":
        return JOKES_SUBREDDIT
    elif type_of_joke == "1":
        return ClEAN_JOKES_SUBREDDIT
    elif type_of_joke == "2":
        return DIRTY_JOKES_SUBREDDIT


def produce(type_of_joke, sort_criteria, number_of_the_joke):
    subreddit = find_subreddit(type_of_joke)
    produce_jokes(subreddit, sort_criteria, number_of_the_joke)
