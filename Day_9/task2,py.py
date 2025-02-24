#TODO-1: Ask the user for input
name = input("What is your name?:")
price = int(input("WHat is your bid?: $"))

bids = {}
#TODO-2:save data into dictionary {name: price}
bids[name]=price
#TODO-3:wheather if new bids need to be added
should_continue = input("Are there any other bidders? Type 'yes' or  'no'.\n")

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
#TODO-4: compare bids in dictionary
def find_height_bidder(bidder_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid
