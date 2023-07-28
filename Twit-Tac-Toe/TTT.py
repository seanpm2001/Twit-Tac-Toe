#!/usr/bin/env python3
# Start of script
# Twit-Tac-Toe
# A simple game of Tic-Tac-Toe, but whoever wins gets to win the decision if it is Twitter or X.
# This is bad code, I used a lot of if statements, and the program may not be functional either way. Please open an issue and give feedback on how to write this program better if you have any ideas.
# Goal: get this program under 140 lines, and keep it that way (current: 162)
# Import section
import os()
import tkinter()
import random()
# Variables
int x = 0
int y = 0
str game = "new" # Status: "new" "ongoing" "X Won" "O Won" "draw" "ended"
# Functions
def x():
    # Asset goes here
    if (game == "new"):
        set x == 0
        break
    while (x < 1 and x > 5):
        game == "ongoing"
        break
def o():
    # Asset goes here
    if (game == "new"):
        set o == 0
    while (o < 1 and o > 5):
        game == "ongoing"
        break
def newGame()
    place1 = input()
    game == "new"
    break
def winOrLose():
    if (x > 4 and o > 4):
        if (game != "X Won" or "O Won"):
            game == "draw"
            return draw()
            break
        else:
            return winOrLose()
def threeInARow():
    if (x > 2):
        user1++
        game == "X Won"
        break
    elif (o > 2):
        user2++
        game == "O Won"
        break
    else:
        return 0
def draw():
    print("The game has ended in a draw.")
    sleep(3000) # Wait for 3 seconds (3000 milliseconds)
    return newGame()
    break
def background():
    if (wallpaperOn == True and wallpaperReset == True):
        set backImg = "/Assets/Background/Twitter1.png" # Pseudocode
    else if (wallpaperOn != True and or wallpaperReset != True):
        return 0
def changeBackground()
    if (backgroundNum > 1):
        backgroundNum == 1
    if (wallpaperTransitions == True):
        if (backgroundNum == 1):
            set backImg = "/Assets/Background/Twitter2.png" # Pseudocode
            break
        elif (backgroundNum == 2):
            if (backgroundNumLimit > 2):
                set backImg = "/Assets/Background/Twitter3.png" # Pseudocode
                if backImg = False # Pseudocode
                    set backImg == "/Assets/Background/Twitter1.png" and backgroundNum == 1 # Pseudocode
                    break
                break
            else:
                set backImg = "/Assets/Background/Twitter1.png" # Pseudocode
                if backImg = False # Pseudocode
                    set backImg == "/Assets/Background/Twitter1.png" and backgroundNum == 1 # Pseudocode
                    break
                break
        elif (backgroundNum == 3):
            if (backgroundNumLimit > 2):
                set backImg = "/Assets/Background/Twitter4.png" # Pseudocode
                if backImg = False # Pseudocode
                    set backImg == "/Assets/Background/Twitter1.png" and backgroundNum == 1 # Pseudocode
                    break
                break
            else:
                set backImg = "/Assets/Background/Twitter1.png" # Pseudocode
                if backImg = False # Pseudocode
                    set body.bgcolor("BLACK") # Pseudocode
                    break
                break
            # There has to be a more efficient way to write this, so I will stop here for now/
def program():
    print("Twit-Tac-Toe")
def menu():
    menu1 = str(input("New game [N] High scores [H] Settings [S] Quit [Q]"))
    menu1.upper()
    if (menu1 == "N"):
        return newGame()
        break
    elif (menu1 == "H"):
        return scoreboard()
        break
    elif (menu1 == "S"):
        return settings()
        break
    elif (menu1 == "Q"):
        game == "ended"
        break
        return endGame()
    else:
        return menu()
        break
def settings():
    wallpaperReset = bool(True)
    wallpaperOn = bool(True)
    wallpaperTransitions = bool(True)
    backgroundNumLimit = int(3)
    backgroundNum = int(1)
    list highscores = ["", ""] # Pseudocode
def endGame():
    if (game != "new"):
        quitD = str(input("Are you sure you want to quit? (y/N)"))
        quitD.upper()
        if (quitD == "Y" or "YES"):
            exit()
        else:
            return menu()
            break
def scoreboard():
    user1 == "Musk" # X
    user2 == "Twitter" # O
    user1Score = 0 # How do I encapsulate this value?
    user2Score = 0 # How do I encapsulate this value?
def about():
    print("Twit-Tac-Toe\n\nVersion 0.1 pre-alpha\n2023, Thursday, July 27th at 6:40 pm PST)\nTwit-Tac-Toe Copyleft 🄯 Seanpm2001 (2023-2023) @seanpm2001\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\nYou should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.")
    abt1 = str(input("Type L and hit enter to see the license, type A and hit enter to reload the about page, type anything else and hit enter to close the about box"))
    abt1.upper()
    if (abt1 == "L" or "LICENSE"):
        os.getfile(/LICENSE.txt)
        break
    elif (abt1 == "A" or "ABOUT"):
        return about()
        break
    else:
        return 0
# Calling all functions and starting the game
return program()
return about()
return menu()
break
# File info
# File version: 1 (2023, Thursday, July 27th at 7:11 pm PST)
# File type: Python source file (*.py)
# Line count (including blank lines and compiler line): 162
# End of script

