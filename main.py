import subprocess


def clear():
    subprocess.call("clear")


continue_biding = True
bids = {}
while continue_biding:
    name = input("What is your name?:\n")
    bid = int(input("What's your bid'?:\n"))
    bids[name] = bid

    continue_biding = not input("Anyone else?:\n").lower() == 'no'
    if continue_biding:
        clear()

max_value = 0
winner = ''

for key in bids:
    if bids[key] > max_value:
        max_value = bids[key]
        winner = key

print(f"the winner is {winner} with bid {max_value}")
