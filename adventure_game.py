import time
import random


# print msg with time
def print_pause(x):

    print(x)
    time.sleep(1)


# start game
def play_game():

    # monster boss, choose random
    monster = random.choice(['Pirate', 'Orc', 'Demon', 'Witch', 'Troll'])

    # list of wepons to deafet the monster and beast
    itens = ["small sword"]

    # small beast to defeat with small sword.
    beast = random.choice(["Wolf", "Bear", "Panther", "Tiger"])

    intro(monster)
    choice(itens, monster, beast)


# error msg
def error():
    print_pause("Sorry, I don't understand")


# back to the field
def back_field(itens, monster, beast):
    print_pause("You walk back to out to the field.")
    choice(itens, monster, beast)


# intro msg
def intro(monster):
    print_pause("You find yourself standing in an open field,"
                "filled with grass and some wildflowers")
    print_pause(f"Rumor has it that a wicked {monster} is somewhere around"
                "here, and has been terrifying the nearby village.")
    print_pause("To your right is a dark cave.")
    print_pause("In front of you is a small florest.")
    print_pause("To your left is a house.")
    print_pause("In your hand you hold your trusty (but not very"
                " effective) Small Sword.\n")


# choices in the field
def choice(itens, monster, beast):

    # n = choice to move
    n = input("Enter 1 to peer into the Cave.\n"
              "Enter 2 to peer the Florest\n"
              "Enter 3 to knock on the door of the House.\n"
              "What would you like to do?\n")

    # option 1 cave
    if n == '1':
        cave(itens, monster, beast)

    # option 2 florest
    elif n == '2':
        florest(itens, monster, beast)

    # option 3 house
    elif n == '3':
        house(itens, monster, beast)

    # invalid option
    else:
        error()
        choice(itens, monster, beast)


# cave actions
def cave(itens, monster, beast):
    print_pause("You peer cautiously into the cave.")

    # check if have Sword of Ogoroth
    if "Sword of Ogoroth" in itens:
        print_pause("You've been here before, and gotten all good stuff.")
        print_pause("It's just an empty cave now.")

    else:
        print_pause("Its turn out to be a small cave.")
        print_pause("You find one big chest.")
        print_pause("You try to open, but need one key.")

        # check if have a key
        if "key" in itens:
            print_pause("Luckly, you have found one key in the waterfall.")
            print_pause("You try the key...")
            print_pause("...")
            print_pause("It works!!!")
            print_pause("Inside of the chest you find the"
                        " magic Sword of Ogoroth!")
            print_pause("You discard your old sword and take"
                        " the Sword of Ogoroth.")
            # change from small sword to Sword of Ogoroth
            itens[0] = "Sword of Ogoroth"

        else:
            print_pause("Unfortunatly, You don't have any key.")

    # back to the field
    back_field(itens, monster, beast)


# florest action
def florest(itens, monster, beast):
    print_pause("You peer into the Florest.")

    # check if have key
    if "key" in itens:
        print_pause(f"You see the dead {beast}. And You know,"
                    " the florest does not have more thing to do.")

    else:
        print_pause("You see a small waterfall, so you go drink some water.")
        print_pause(f"From nowhere some {beast} attacks you.")
        print_pause(f"You must deffend yourself, so you hold"
                    f" your Sword and kill the {beast}.")
        print_pause("So you finally go drink your water,"
                    " when do you find one Key.")
        print_pause("You pick the key.")

        # add key
        itens.append("key")

    # back to the field
    back_field(itens, monster, beast)


# house action
def house(itens, monster, beast):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                f" opens and out steps a {monster}.")
    print_pause(f"Yeap! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")

    # have the Sword of Ogoroth
    if "Sword of Ogoroth" in itens:
        win_loose(itens, monster, beast)

    else:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a Small Sword.")
        win_loose(itens, monster, beast)


# win loose situation
def win_loose(itens, monster, beast):
    decision = input("What would you like to do?\n"
                     "(1) Fight\n"
                     "(2) Run Away \n")

    # fight
    if decision == '1':

        # have the Sword of Ogoroth
        if "Sword of Ogoroth" in itens:
            print_pause(f"As the {monster} moves to attack, you"
                        " unsheat your new sword")
            print_pause("The Sword of Ogoroth shines brightly in your"
                        " handas you brace for your \nfor the attack.")
            print_pause(f"But the {monster} try to scape, but with"
                        f" only one blow you kill the {monster}.")
            print_pause(f"You have rid the town of the {monster}.")
            print_pause("YOU ARE VICTORIOUS!!!")

        else:
            print_pause("You do your best....")
            print_pause(f"But your sword is no match for the {monster}.")
            print_pause("You have been defeated!!!")

    # runaway
    elif decision == '2':
        print_pause(f"You run away, and you lost the {monster} of the view.")
        print_pause(f"Luckily, the {monster} didn't follow you.")
        # back to the field
        back_field(itens, monster, beast)

    else:
        # error msg
        error()
        win_loose(itens, monster, beast)


# play again
def play_again():
    response = input("Would you like to play again?\n"
                     "Type 'YES' or 'NO'.\n").lower()

    box = ['yes', 'no']

    while response not in box:
        # error msg
        error()
        return play_again()

    if "no" in response:
        print_pause("Tanks for playing. See you next time.")

    # start the game again
    elif "yes" in response:
        print_pause("Excellent!! Restarting the game.")
        # start the game again
        adventure()


# full game
def adventure():
    play_game()
    play_again()


if __name__ == "__main__":
    adventure()
