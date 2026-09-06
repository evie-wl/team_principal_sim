"""Team principal simulator"""
# Advanced Processes
# Evie W
# 3/08

import random

def display_drivers(drivers):
    """Print a clean report of driver information."""

    # Print title for user
    print("\n--- Driver Stats ---")

    # Print a clean display
    for data in drivers:
        print(("Name: {} | Speed: {} | Racecraft: {} Aggressive: {} |").format(
            data["name"], data["speed"], data["racecraft"], data["aggressive"]))
        
def display_costs(drivers, balance):
    """Print a clean report of driver prices"""

    # Print title and balance for user
    print("\n--- Driver Costs ---")
    print(balance)

    # Print out all drivers and their cost in a clean display
    for data in drivers:
         print(("Name: {} | Cost: {} million").format(data["name"], data["cost"]))


def buy_drivers(drivers, balance, player_profile):
    """Allow drivers to buy two drivers"""
    
    # Print titles for user
    print("\n--- Driver Purchase ---")

    # Ask user which driver they would like to buy
    choice = input("Enter the first name of the driver you would like to purchase: ").strip().lower()

    
    for data in drivers:
        # If user choice does not equal a drivers first name, go to the next one
        if choice != data["name"].split()[0]:
            continue

        # Check if they have already bought the driver
        if data["stock"] <= 0:
            print("Sorry, you have already bought this driver.")
            return balance
        
        # Get the set cost of prize user chose
        charge = data["cost"]

        # Check if the player has enough tickets to afford it
        if balance < charge:
            print("Sorry, you don't have enough money to buy this driver.")
            return balance

        # Remove driver from stock so they can't buy again
        data["stock"] -= 1
        
        # Update the users balance and profile with their new driver
        if player_profile["driver_one"] == "":
            player_profile["driver_one"] = choice
        else:
            player_profile["driver_two"] = choice

        balance = balance - charge

        # Message of success and balance return
        print(("You have successfully bought {} for your team").format(choice))
        return balance

    # Message if user enters a name that is not one of the drivers'
    print("That driver does not exist! Please try again.")
    return balance


def race_sim(drivers, player_profile, balance):
    """Simulate a race"""

    # Print titles for user
    print("\n--- Race Simulation ---")
    print("------------------------")
    print("Australian Grand Prix Results")

    results = []

    # Go through all the drivers
    for driver in drivers:

        # Calculate score using driver stats
        scoring = (driver["speed"] * 0.5 + driver["racecraft"] * 0.3 + driver["aggressive"] * 0.2)

        # Add race day luck
        scoring += random.randint(-3, 3)

        # Add result to the results list
        results.append({"name": driver["name"], "scoring": scoring})
        
    # Variable for positions
    position = 1

    # Start loop for drivers in results
    while results:
        highest = results[0]
    
        # Sort drivers
        for result in results:
            if result["scoring"] > highest["scoring"]:
                highest = result

        # Print drivers
        print(position, "-", highest["name"])

        # Check for P1 driver
        if position == 1:

            # Check users drivers agains highest
            if highest["name"].split()[0] == player_profile["driver_one"] or highest["name"].split()[0] == player_profile["driver_two"]:

                # Print
                print("Congrats on your win, you get 5 million")
                balance += 5

        # Reset variables
        results.remove(highest)
        position += 1

    return balance
    
def team_info(player_profile):
    """Users can see their team"""

    # Print titles for user
    print("\n--- Team Information ---")
    print("------------------------")

    # Print info    
    print("Driver one:", player_profile["driver_one"])
    print("Driver two:", player_profile["driver_two"])        

def track_info():
    """Australia track information"""
    
    # Print titles for user
    print("\n--- Track Information ---")
    print("------------------------")

    # Print out the info
    print("Track: Australia")
    print("Speed: 5/10")
    print("Racecraft: 4/10")
    print("Aggressive: 2/10")
        
def main():

    # Set up variables
    player_profile = {"driver_one": "" , "driver_two": ""}
    balance = 30
    drivers = [
        {"ID": 1, "name": "lando norizz", "speed": 94, "racecraft": 90, "aggressive": 82, "cost":15, "stock": 1},
        {"ID": 2, "name": "charles lecorrect", "speed": 96, "racecraft": 88, "aggressive": 84, "cost":17, "stock": 1},
        {"ID": 3, "name": "liam lawsuit", "speed": 87, "racecraft": 86, "aggressive": 90, "cost":7, "stock": 1},
        {"ID": 4, "name": "max verstopping", "speed": 99, "racecraft": 97, "aggressive": 94, "cost":22, "stock": 1},
        {"ID": 5, "name": "issac badjar", "speed": 88, "racecraft": 85, "aggressive": 87, "cost":8, "stock": 1},
        {"ID": 6, "name": "george russelling", "speed": 93, "racecraft": 89, "aggressive": 85, "cost":13, "stock": 1},
        {"ID": 7, "name": "kimi antonoodle", "speed": 92, "racecraft": 88, "aggressive": 84, "cost":11, "stock": 1},
        {"ID": 8, "name": "lewis hamiltown", "speed": 91, "racecraft": 96, "aggressive": 83, "cost":14, "stock": 1}
    ]

    # Welcome the players
    print("Welcome to the racing team principal simulator!")
    print(("Your starting balance is: {} million").format(balance))

    # Start program menu loop
    while True:

        # User can see menu options displayed
        print("\n--- Team principal simulator ---")
        print("1) display drivers stats")
        print("2) display drivers costs")
        print("3) buy drivers")
        print("4) simulate race")
        print("5) team info")
        print("6) track information")
        print("0) exit")
        print("---")

        # User can see current balance displayed
        print(("current balance: {} million").format(balance))

        user_choice = input("Choose an option 1, 2, 3, 4, 0: ")

        # End the program
        if user_choice == "0":
            print("Goodbye!")
            break

        # Choices
        elif user_choice == "1":
            display_drivers(drivers)

        elif user_choice == "2":
            display_costs(drivers, balance)

        elif user_choice == "3":
            print("Choose your first driver")
            balance = buy_drivers(drivers, balance, player_profile)

            print("Choose your second driver")
            balance = buy_drivers(drivers, balance, player_profile)

        elif user_choice == "4":
            balance = race_sim(drivers, player_profile, balance)

        elif user_choice == "5":
            team_info(player_profile)
            

        elif user_choice == "6":
            track_info()


if __name__ == "__main__":
    main()
