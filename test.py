import random
import os


def wichteln_auto():
    os.system("cls")
    names = ["Taylan", "Tacım", "Ezgi", "Serhat", "Gülistan", "Roşin", "Muhi"]
    to_be_drawn = ["Taylan", "Tacım", "Ezgi",
                   "Serhat", "Gülistan", "Roşin", "Muhi"]
    while names != []:
        enter_first = input(
            "Merhaba {}, isim çekmek için ENTER tuşuna bas: ".format(names[0]))
        current_user = names[0]
        names.remove(current_user)
        if [current_user] == to_be_drawn:
            print("Kendini çektin, lütfen baştan başla!")
            start_over = input("Bitirmek için ENTER tuşuna bas: ")
            return "Muziplik tamamlanmadı :("
        elif current_user in to_be_drawn:
            to_be_drawn.remove(current_user)
            random_x = random.choice(to_be_drawn)
            to_be_drawn.append(current_user)
        else:
            random_x = random.choice(to_be_drawn)
        print("{} sana çıkan isim: {} \nLütfen ismi bir yere not al.".format(
            current_user, random_x))
        random_selected = random_x
        to_be_drawn.remove(random_selected)
        next_user = input(
            "Ekranı silmek için hazır olduğunda ENTER tuşuna bas: ")
        os.system("cls")
    return "Muziplik tamamlandı :)"


print(wichteln_auto())
