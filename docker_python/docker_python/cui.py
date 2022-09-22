from producer import produce


def second_screen(choice):
    type_of_joke, sort_criteria, number_of_the_joke = choice.split(' ')
    produce(type_of_joke, sort_criteria, number_of_the_joke)
    print("Do you wanna hear another joke?")
    print("0 - Yes")
    print("1 - No")
    decision = input()
    if decision == "0":
        first_screen()


def first_screen():
    print("Input should look like:")
    print("x y z")
    print("x - value from 0 to 2, where 0 - a standard joke, 1 - a clean joke, 2 - a dirty joke")
    print("y - value from 0 to 3, where 0 - hot, 1 - top, 2 - new, 3 - rising")
    print("z - value from 0 to 99, where z is number of the joke you want to read")
    choice = input()
    second_screen(choice)


if __name__ == "__main__":
    print("============")
    print("REDDIT JOKES")
    print("============")
    first_screen()
