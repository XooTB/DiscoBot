import csv
import random
import string
import db

# def get_random_string():
#     # Random string with the combination of lower and upper case
#     letters = string.ascii_letters
#     result_str = ''.join(random.choice(letters) for i in range(5))
#     return result_str


def place_bet(name, amount, odds, betted):
    while 1:
        if db.member_exists(name):
            member_balance = db.check_balance(name)
            if member_balance >= amount:
                db.add_bet(name, amount, odds, betted)
                db.update_balance(name, member_balance - amount)
                break
            else:
                pass
        else:
            db.add_member(name)
            continue
