bids = {}


def find_highest_bidder(bidding_dic):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_dic.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while True:
    name = input("What is your name? ")
    amount = int(input("Amount you want to bid $"))
    bids[name] = amount

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 10)

    if should_continue == "no":
        break


find_highest_bidder(bids)