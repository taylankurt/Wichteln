import random
import os


# print(names_len)


def wichtel():
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
                if name in to_be_drawn:
                    to_be_drawn.remove(name)
                    random_x = random.choice(to_be_drawn)
                    to_be_drawn.append(name)
                elif name not in to_be_drawn:
                    random_x = random.choice(to_be_drawn)
                print("{} you have {}".format(name, random_x))
                random_selected = random_x
                to_be_drawn.remove(random_selected)
                next_user = input("Please enter any key: ")
                os.system("cls")
                draw_count = draw_count + 1
    return "Mischief managed!"


print(wichtel())
