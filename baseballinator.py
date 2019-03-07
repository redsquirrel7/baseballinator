#!/usr/bin/env python
#
# __________                     ___.          .__  .__  .__               __                
#\______   \_____    ______ ____\_ |__ _____  |  | |  | |__| ____ _____ _/  |_  ___________ 
# |    |  _/\__  \  /  ___// __ \| __ \\__  \ |  | |  | |  |/    \\__  \\   __\/  _ \_  __ \
# |    |   \ / __ \_\___ \\  ___/| \_\ \/ __ \|  |_|  |_|  |   |  \/ __ \|  | (  <_> )  | \/
# |______  /(____  /____  >\___  >___  (____  /____/____/__|___|  (____  /__|  \____/|__|   
# \/      \/     \/     \/    \/     \/                  \/     \/                   
#                                                                                          v1.1
# 
# By: Brad Nelson (@resquirrel_7)
# Baseball program for Aaron at the Sweets.

import os.path
from pathlib import Path

# Check to see if txt files exist. If not, create them.
def file_check(fname):
    if fname.exists():
        print(str(fname), 'exists')
#        f = str(fname)
#        reset_start(f)
    else:
        print(str(fname), 'Does not exist. Creating...')
        f = open(str(fname),"w")
        f.write("0")
        f.close()

# Not sure why this isn't working...
# I don't have time to figure it out right now.
#
#def reset_start(fname):
#    print("Would you like to reset it?")
#    choice = input("[y/n] ")
#    if str(choice) == "y":
#        reset_num(fname)
#    elif str(choice) == "n":
#        print("Not resetting")
#    else:
#        print("That is not an option. Try again...")
#        reset_start()

# Increase number in file.
def increase_num(fname):
    f = open(str(fname),"r")
    num = f.read(1)
    f.close()
    f = open(str(fname),"w")
    newnum = int(num) + 1
    f.write(str(newnum))
    f.close()


# Reset number in file.
def reset_num(fname):
    f = open(str(fname),"w")
    f.write("0")
    f.close()


# Decrease number in file (just in case).
def decrease_num(fname):
    f = open(str(fname),"r")
    num = f.read(1)
    f.close()
    f = open(str(fname),"w")
    newnum = int(num) - 1
    f.write(str(newnum))
    f.close()

# Display menu and get input from user.

def main_menu():
    print("Welcome! Please choose an opion.")
    print("--------------------------------")
    print(" ")
    print("1 - Add to Balls")
    print("2 - Add to Strikes")
    print("3 - Add to Outs")
    print("4 - Subtract from Balls")
    print("5 - Subtract from Strikes")
    print("6 - Subtract from Outs")
    print("7 - Reset Balls")
    print("8 - Reset Strikes")
    print("9 - Reset Outs")
    print("10 - Add to Innings")
    print("11 - Subtract from Innings")
    print("12 - Reset Innings")
    print("0 - Exit")

    choice = input("> ")
    if str(choice) == "1":
        txt = Path("./balls.txt")
        increase_num(txt)
        print("The balls have increased!")
        main_menu()
    elif str(choice) == "2":
        txt = Path("./strikes.txt")
        increase_num(txt)
        print("The strikes have increased!")
        main_menu()
    elif str(choice) == "3":
        txt = Path("./outs.txt")
        increase_num(txt)
        print("The outs have increased!")
        main_menu()
    elif str(choice) == "4":
        txt = Path("./balls.txt")
        decrease_num(txt)
        print("The balls have decreased!")
        main_menu()
    elif str(choice) == "5":
        txt = Path("./strikes.txt")
        decrease_num(txt)
        print("The strikes have decreased!")
        main_menu()
    elif str(choice) == "6":
        txt = Path("./outs.txt")
        decrease_num(txt)
        print("The outs have decreased!")
        main_menu()
    elif str(choice) == "7":
        txt = Path("./balls.txt")
        reset_num(txt)
        print("The balls have been reset to 0!")
        main_menu()
    elif str(choice) == "8":
        txt = Path("./strikes")
        reset_num(txt)
        print("The strikes have been reset to 0!")
        main_menu()
    elif str(choice) == "9":
        txt = Path("./outs.txt")
        reset_num(txt)
        print("The outs have been reset to 0!")
        main_menu()
    elif str(choice) == "10":
        txt = Path("./innings.txt")
        increase_num(txt)
        print("The innings have increased!")
        main_menu()
    elif str(choice) == "11":
        txt = Path("./innings.txt")
        decrease_num(txt)
        print("The innings have decreased!")
        main_menu()
    elif str(choice) == "12":
        txt = Path("./innings.txt")
        reset_num(txt)
        print("The innings have been reset to 0!")
        main_menu()
    elif str(choice) == "0":
        exit()
    else:
        print("You done messed up A-A-RON!!!")
        print("That is not an option!")
        main_menu()

print("Checking text files...")
balls = Path("./balls.txt")
strikes = Path("./strikes.txt")
outs = Path("./outs.txt")
innings = Path("./innings.txt")
file_check(balls)
file_check(strikes)
file_check(outs)
file_check(innings)
main_menu()
