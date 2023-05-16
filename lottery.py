import random

arr = list(range(1, 90))
winning_ticket = random.sample(arr, 5)

print(f"Winning Draw for today is {winning_ticket}.")
