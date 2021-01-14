import sqlite3

conn = sqlite3.connect('sheets/main.db')

c = conn.cursor()

# c.execute(""" CREATE TABLE ongoing_bets (
#         username text,
#         bet float,
#         odds float,
#         win_amount float
#         )""")

# c.execute(""" CREATE TABLE balance_sheet (
#         username text,
#         balance float
#         )""")

# conn.commit()


def add_member(name):
    c.execute(f"INSERT INTO balance_sheet VALUES ('{name}',200)")
    conn.commit()
    print('New Member Added!')


def check_balance(name):
    c.execute(f"SELECT * FROM balance_sheet WHERE username = '{name}'")
    return c.fetchone()[1]


def member_exists(name):
    c.execute(f"SELECT * FROM balance_sheet WHERE username = '{name}'")
    if c.fetchone():
        return True
    else:
        return False


def update_balance(name, amount):
    c.execute(
        f"UPDATE balance_sheet SET balance = {amount} WHERE username = '{name}'")
    conn.commit()
    # print('Balance Updated!')


def add_bet(name, amount, odds, betted):
    c.execute(
        f"INSERT INTO ongoing_bets VALUES ('{name}',{amount},'{odds}',{amount*odds}, {betted})")
    conn.commit()
    print('Successfully added!')


def on_win(name):
    c.execute(f"SELECT win_amount FROM ongoing_bets WHERE username = '{name}'")
    print(c.fetchone())
