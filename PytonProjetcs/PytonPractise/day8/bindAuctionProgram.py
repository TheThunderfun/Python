
from art import logo

print(logo)
print("Welcome to the secret auction program.")

continue_auction = True

def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0 
    max(bidding_record)
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while continue_auction == "yes":
    
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    bids= {}
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_auction = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)