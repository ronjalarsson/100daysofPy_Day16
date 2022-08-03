from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off = False

# Create objects that are needed
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
while not turn_off:
    # Check the user’s input to decide what to do next.
    options = menu.get_items()
    option = input(f"What would you like? ({options}): ")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # Your code should end execution when this happens.
    if option == "off":
        turn_off = True
    # TODO: 3. Print report.
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif option == "report":
        coffee_machine.report()  # Call the report() method in coffee_machin object to get the details of ingredients.
        money_machine.report()  # Call the report() method in money_machine object to get the amount of money received.
    else:
        # TODO: 4. Check resources sufficient?
        drink = menu.find_drink(option)  # The user input "option" is stored in variable drink.
        # When the user chooses a drink, the program checks if there are enough resources to make that drink.
        if coffee_machine.is_resource_sufficient(drink):
            # TODO: 5. Process coins.
            # If there are sufficient resources to make the drink selected,
            # then the program prompts the user to insert coins.
            # TODO: 6. Check transaction successful?
            # Check that the user has inserted enough money to purchase the drink they selected.
            if money_machine.make_payment(drink.cost):
                # Above todos 5 and 6 are included in the method make_payment() in money_machine object
                # TODO: 7. Make Coffee.
                coffee_machine.make_coffee(drink)  # Call the make_coffee() method
                # to deduct the resources and the coffee is made.
