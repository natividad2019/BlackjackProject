
import os
import art1

print(art1.logo)

bids = {} # bids refers to the amount of money that people are willing to pay to win an item in auction. 
bidding_finished = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = "" # this sets the starting winer to an empty string
    print("Bidding Record:", bidding_record)
    for bidder in bidding_record: # This loops through each person(bidder) in the bidding record
        bid_amount = bidding_record[bidder] # This gets the bid amount of the current bidder
        print(f"checking {bidder}'s bid of ${bid_amount}")
        if bid_amount > highest_bid:  # This checks if the current bid amount is higher than the highest bid record so far
            highest_bid = bid_amount # if true, this updates the highest bid to the current bid amount
            winner = bidder #  if true, this updates the winner to the current bidder .
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished: # This starts a loop that continues until `bidding_finished` is true.
    name = input("What is your name?: ") # This asks the user for their name and stores it in the variable `name`.
    price = int(input("What is your bid?: $")) # This asks the user for their bid amount, converts it to an integer and stores in the variable `price`.
    bids[name] = price # This adds the name and bid amount to the `bids` dictionary.
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n") # This asks if there are any other bidders.
    if should_continue == "no": # This checks if the user typed "no".
        bidding_finished = True # if true, this sets `bidding_finished` to True to stop the loop
        find_highest_bidder(bids) # this calls the 'find_highest_bider' function with the 'bids' dictionary  to find the print the highest bidder.
    elif should_continue == "yes": # This checks if the user typed "yes".
        clear() # if true, this clears the screen for next bidder

