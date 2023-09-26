# Visa 2024 summer intern application

# given a list of inventory changes, return the list of revenue from each sale

# TLE with complex add, not sure if this would work now
from collections import defaultdict
from queue import PriorityQueue
def solve(logs):
    revenue = []
    inventory = defaultdict(PriorityQueue)
    if logs[0] == "supply":
        product = logs[1]
        count = int(logs[2])
        price = int(logs[3])
        inventory[product].put((price, count)) # originally added in complex way, can just add another entry of same price!
    elif logs[1] == "sale":
        product = logs[1]
        count = int(logs[2])
        transaction = 0
        while count > 0:
            price, stock = inventory[product].get()
            if stock > count:
                transaction += price * count
                inventory[product].put((price, stock - count))
                count = 0
            else:
                transaction += price * stock
                count -= stock
    elif logs[0] == "return":
        product = logs[1]
        count = int(logs[2])
        price = int(logs[3])
        inventory[product].put((price, count))
    return revenue