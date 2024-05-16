import pandas as pd
from functools import reduce
import math
import random

users_list = [
    {"login": "user1", "share": 1},
    {"login": "user2", "share": 1},
    {"login": "user3", "share": 1},
    {"login": "user4", "share": 1},
    {"login": "user5", "share": 1},
    {"login": "user6", "share": 1},
    {"login": "user7", "share": 1},
    {"login": "user8", "share": 0.5},
    {"login": "user9", "share": 0.5},
    {"login": "user10", "share": 0.5},
]

ASIN_COUNT = 2443


def pick_random(list_of_users):
    return random.choice(list_of_users)


def count_divide_factor(users):
    normal_allocation_users = 0
    half_allocation_users = 0
    for user in users:
        if user["share"] == 1:
            normal_allocation_users += 1
        elif user["share"] == 0.5:
            half_allocation_users += 1
    divisor = normal_allocation_users * 1 + half_allocation_users * 0.5
    return ASIN_COUNT / divisor


def assign_allocation_to_user(users):
    users_with_allocation_amount = []
    divide_factor = count_divide_factor(users)

    for user in users:
        login = user["login"]
        amount = divide_factor * user["share"]
        users_with_allocation_amount.append(
            {"login": login, "amount": math.trunc(amount)}
        )
    total_amount = reduce(
        lambda acc, user: acc + user["amount"], users_with_allocation_amount, 0
    )
    reminder = ASIN_COUNT - total_amount
    random_user = pick_random(users_with_allocation_amount)
    random_user["amount"] += reminder
    print(*users_with_allocation_amount, sep="\n")
    print(total_amount)


assign_allocation_to_user(users_list)
