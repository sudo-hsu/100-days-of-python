from menu import MENU


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(MENU["espresso"]["ingredients"])

# TODO: 1. Print report of all coffee machine resources
def report(resources, machine_money):
    for item in resources:
        if item == "water" or item == "milk":
            print(f"{item.title()}: {resources[item]}ml")
        if item == "coffee":
            print(f"{item.title()}: {resources[item]}g")
    print(f"Money: {machine_money}")


# TODO: 2. Check resources sufficient to make drink order.
def drink_cost(drink_input):
    if drink_input == "report":
        return
    else:
        cost = MENU[drink_input]["cost"]
        return cost


def get_ingredients(drink_input):
    recipe = MENU[drink_input]["ingredients"]
    return recipe

get_ingredients("espresso")


#This returns the amount of resources left after a recipe
def calc_resources(resources, recipe):
    for ingredient in recipe:
        resources[ingredient] -= recipe[ingredient]
    return resources


# TODO: 3. Process coins.
def count_money():
    total_money = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_money = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    return total_money

# TODO: 4. Check if transaction is successful.
def check_transaction(cost, total_money):
    if total_money >= cost:
        change = total_money - cost
        print(f"Here is ${change} in change.")
        return 1
    elif cost > total_money:
        print("Sorry, that's not enough money. Money refunded.")
        return 0

def check_resources(resources):
    for item in resources:
        if resources[item] < 0:
            print(f"Sorry, there is not enough {item}.")
            return 0
        else:
            return 1


# TODO: 5. Make drink, subtract resources, and save money total.
end_program = False
machine_money = 0
while not end_program:
    drink_input = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_input == "report":
        report(resources, machine_money)
    elif drink_input == "off":
        end_program = True
    else:
        recipe = get_ingredients(drink_input)
        resources = calc_resources(resources, recipe)
        if check_resources(resources) == 0:
            end_program = True
        else:
            total_money = count_money()
            cost = drink_cost(drink_input)
            if check_transaction(cost, total_money) == 1:
                total_money -= cost
                machine_money += cost
                print(f"Here is your {drink_input}. Enjoy!")



# TODO: 6. Maintenance user can turn off machine using 'off' command.

# TODO: 7. Run program and ask for user input. Allow maintenance to turn off machine using 'off' command.