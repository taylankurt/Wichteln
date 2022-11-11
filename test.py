import random
import os


def wichtel():
    draw_count = 0
    names = ["Taylan", "Tacim", "Ezgi", "Serhat", "Gülistan", "Muhi"]
    to_be_drawn = ["Taylan", "Tacim", "Ezgi", "Serhat", "Gülistan", "Muhi"]
    while draw_count < 6:
        press_key1 = input("{} please press ENTER: ".format(names[0]))
        current_user = names[0]
        if current_user in names:
            names.remove(current_user)
            if current_user in to_be_drawn:
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


print(wichtel())
