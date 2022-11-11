import random
import os


def wichteln_input():
    draw_count = 0
    has_drawn = []
    draw_list = ["Taylan", "Tacim", "Ezgi", "Serhat", "Gülistan", "Muhi"]
    to_be_drawn = ["Taylan", "Tacim", "Ezgi", "Serhat", "Gülistan", "Muhi"]
    while draw_count < 6:
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
                    start_over = input("Please press ENTER to end: ")
                    return "Mischief not managed :("
                elif name in to_be_drawn:
                    to_be_drawn.remove(name)
                    random_x = random.choice(to_be_drawn)
                    to_be_drawn.append(name)
                else:
                    random_x = random.choice(to_be_drawn)
                print("{} you have {}".format(name, random_x))
                random_selected = random_x
                to_be_drawn.remove(random_selected)
                next_user = input("Please enter any key: ")
                os.system("cls")
                draw_count = draw_count + 1
    return "Mischief managed!"


def wichteln_auto():
    draw_count = 0
    names = ["Taylan", "Tacim", "Ezgi", "Serhat", "Gülistan", "Muhi"]
    to_be_drawn = ["Taylan", "Tacim", "Ezgi", "Serhat", "Gülistan", "Muhi"]
    while draw_count < 6:
        enter_first = input("{} please press ENTER: ".format(names[0]))
        current_user = names[0]
        names.remove(current_user)
        if [current_user] == to_be_drawn:
            print("You have drawn yourself, please start over again!")
            start_over = input("Please press ENTER to end: ")
            return "Mischief not managed :("
        elif current_user in to_be_drawn:
            to_be_drawn.remove(current_user)
            random_x = random.choice(to_be_drawn)
            to_be_drawn.append(current_user)
        else:
            random_x = random.choice(to_be_drawn)
        print("{} you have {}".format(current_user, random_x))
        random_selected = random_x
        to_be_drawn.remove(random_selected)
        next_user = input("Please press ENTER: ")
        os.system("cls")
        draw_count = draw_count + 1
    return "Mischief managed!"


print("test")
print(wichteln_auto())
