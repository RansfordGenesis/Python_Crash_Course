import random

count = 0
i = 0
arr = list(range(1, 90))
my_ticket = [33,66, 52]

while i != 1:
    winning_ticket = random.sample(arr, 3)
    count += 1
    if winning_ticket == my_ticket:
        print(f"Congratulations, you've the winning number: {winning_ticket} after {count} days.")
        break
    
        