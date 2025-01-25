import data

#Initialize code by getting data from the original report
coffee_menu = data.MENU
coffee_menu["espresso"]["ingredients"]["milk"] = 0
resources = data.resources
resources["money"] = 0

#Checks the inserted coins and adds them together to calculate the total
def check_coins():
    print("Please insert coins.")
    penny = int(input("How many pennies?"))
    nickel = int(input("How many nickels?"))
    dime = int(input("How many dimes?"))
    quarter = int(input("How many quarters?"))
    amount_given = penny*.01 + nickel*.05 + dime*.10 + quarter*.25
    return amount_given

#Checks the current resources in the machine and outputs something if there is not enough or nothing if it is fine
def check_resources(drink_order, coffee_menu, resources):
    needs = coffee_menu[drink_order]["ingredients"]
    if needs["water"] > resources["water"]:
        return "Sorry there is not enough water."
    elif needs["milk"] > resources["milk"]:
        return "Sorry there is not enough milk."
    elif needs["coffee"] > resources["coffee"]:
        return "Sorry there is not enough coffee."
    else:
        return

#Makes coffee and subtracts the used ingredints from the coffee machines resources
def make_coffee(drink_order, coffee_menu, resources):
    new_milk = resources["milk"] - coffee_menu[drink_order]["ingredients"]["milk"]
    new_coffee = resources["coffee"] - coffee_menu[drink_order]["ingredients"]["coffee"]
    new_water = resources["water"] - coffee_menu[drink_order]["ingredients"]["water"]
    resources["milk"] = new_milk
    resources["coffee"] = new_coffee
    resources["water"] = new_water
    return resources

is_on = True
while is_on:
    drink_order = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_order == "OFF":
        is_on = False
    elif drink_order == "report":
        print(resources)
    else:
        check_resources(drink_order, coffee_menu, resources)
        total = check_coins()
        if total == coffee_menu[drink_order]["cost"]:
            resources["money"] += total
            make_coffee(drink_order, coffee_menu, resources)
            print(f"Here is your {drink_order}! Enjoy")
        elif total > coffee_menu[drink_order]["cost"]:
            change = round(total - coffee_menu[drink_order]["cost"], 2)
            resources["money"] += total - change
            print(f"Here is {change} dollars in change.")
            make_coffee(drink_order, coffee_menu, resources)
            print(f"Here is your {drink_order}! Enjoy")
        else:
            print("Sorry that is not enough money. Money refunded.")