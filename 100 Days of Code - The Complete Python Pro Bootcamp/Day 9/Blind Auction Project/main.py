# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def auction_checker(auction_list):
    val_list = list(auction_list.values())
    max_val = max(val_list)
    max_index = val_list.index(max_val)
    key = list(auction_list.keys())
    person = key[max_index]
    print(f"The winner is {person} with a bid of ${max_val}")


auction_list = {}
amount = []
program_run = True

while program_run:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    auction_list[name] = bid
    other = input("Are there any other bidders? Type yes or no.")
    if other == "yes":
        print("\n" * 20)
    else:
        auction_checker(auction_list)
        program_run = False
