import random
import os


def wichteln_input():
    os.system("clear")
    has_drawn = []
    draw_list = ["Taylan", "Tacim", "Ezgi",
                 "Serhat", "Gülistan", "Roşin", "Muhi"]
    to_be_drawn = ["Taylan", "Tacim", "Ezgi",
                   "Serhat", "Gülistan", "Roşin", "Muhi"]
    while to_be_drawn != []:
        name = input("Please write your name: ").capitalize().strip()
        if name in has_drawn:
            print("{} you got already a name!, please write another name".format(name))
        elif name not in draw_list:
            print("Please enter a valid name")
        else:
            if name in draw_list:
                has_drawn.append(name)
                if [name] == to_be_drawn:
                    print("You have drawn yourself, please start over again!")
                    input("Please press ENTER to end: ")
                    return "Mischief not managed :("
                if name in to_be_drawn:
                    to_be_drawn.remove(name)
                    random_x = random.choice(to_be_drawn)
                    to_be_drawn.append(name)
                else:
                    random_x = random.choice(to_be_drawn)
                print("{} you have {}".format(name, random_x))
                random_selected = random_x
                to_be_drawn.remove(random_selected)
                input("Please enter any key: ")
                os.system("clear")
    return "Mischief managed!"


def wichteln_auto():
    os.system("clear")
    names = ["Taylan", "Tacim", "Ezgi", "Serhat", "Gülistan", "Roşin", "Muhi"]
    to_be_drawn = ["Taylan", "Tacim", "Ezgi",
                   "Serhat", "Gülistan", "Roşin", "Muhi"]
    while names != []:
        input(
            "Hi {}, press ENTER to get your name: ".format(names[0]))
        current_user = names[0]
        names.remove(current_user)
        if [current_user] == to_be_drawn:
            print("You have drawn yourself, please start over again!")
            input("Please press ENTER to end: ")
            return "Mischief not managed :("
        if current_user in to_be_drawn:
            to_be_drawn.remove(current_user)
            random_x = random.choice(to_be_drawn)
            to_be_drawn.append(current_user)
        else:
            random_x = random.choice(to_be_drawn)
        print("{} you have drawn: {} \nPlease note the name.".format(
            current_user, random_x))
        random_selected = random_x
        to_be_drawn.remove(random_selected)
        input(
            "When ready press ENTER to wipe the screen: ")
        os.system("clear")
    return "Mischief managed!"


print(wichteln_auto())
