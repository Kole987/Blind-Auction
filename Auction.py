def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)
from art import logo
print(logo)
newbidders = True
bidders ={}
while newbidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    clear()
    newbid = input("Is there other bidders?: ")
    if newbid == "no":
        newbidders = False
        x=0
        for key in bidders:
            if x >= bidders[key]:
                x = bidders[key]
        print(f"The winner is {key} with a bid of ${bidders[key]}")



