import art
from game_data import data
import random
import subprocess


def clear():
    subprocess.call("clear")


def get_next(list_data:list):
    array_len = len(list_data)
    index = random.randint(0, array_len - 1)
    return list_data.pop(index)


def check_input(a, b, bid):
    if bid.lower() == "a":
        object_1 = a
        object_2 = b
    else:
        object_1 = b
        object_2 = a

    if object_1["follower_count"] == object_2["follower_count"]:
        return "equal"
    elif object_1["follower_count"] > object_2["follower_count"]:
        return "You're right"
    else:
        return "Sorry, that's wrong"


remains = len(data)
user_score = 0
lost = False
object_a = get_next(data)

while remains > 1 and lost is False:
    object_b = get_next(data)
    remains = len(data)

    print(art.logo)
    print("Compare A: {}, a {}, from {} score {}".format(object_a["name"], object_a["description"], object_a["country"],
                                                         object_a["follower_count"]))
    print(art.vs)
    print("Against B: {}, a {}, from {} score {}".format(object_b["name"], object_b["description"], object_b["country"],
                                                         object_b["follower_count"]))

    user_choice = input("Who has more followers: A or B?: ")

    result = check_input(object_a, object_b, user_choice)

    if result.lower() == "Sorry, that's wrong".lower():
        lost = True
        print("{}. Your score = {}".format(result, user_score))
    else:
        user_score += 1
        print("{}. Your score = {}".format(result, user_score))
        object_a = object_b
        object_b = get_next(data)
        clear()

clear()

