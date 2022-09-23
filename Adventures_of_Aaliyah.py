"""
Text-based adventure by Feargal Downey
Adventures Of Aaliyah
Created in Python 3.7.9
Date 17/09/21
"""

import time
import random
import sys
words = " "

def faketype(words):
  words
  for char in words:
    time.sleep(random.choice([0.055]))
    sys.stdout.write(char)
    sys.stdout.flush()
  time.sleep(1)



greg_rp = 0

def start():
  # give some prompts.
  faketype("\n.....\n...\nA young girl grimaces as her eyes struggle to open in the harsh sunlight.")
  faketype("\nShe clutches a nearby railing to pull herself up.")
  faketype("\nThe girl stood up, and within a moment her heart drops...\n\nShuddering as she glances around.")
  faketype("\nThe smell worse now, then the sight of it.")
  faketype("\nWill the girl get sick or will she brave the conditions? ")
  answer = input("\ns - to get sick\nb - to brave conditions  > ").lower()  # convert the player's input() to lower_case

  

  if "b" in answer:
    # if player typed "s" gain 1 rp from Greg
    greg_rp_up()
  elif "s" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    greg_rp_down()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")



# bear room
def greg_rp_up():
  # give some prompts
  faketype("\n\"Huh... I'm Impressed...\"\n\"Would have expected a girl your age to be sick at this sight.\"")

  
  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("The bear killed you.")
  elif answer == "2":
    # lead him to the diamond_room()
    faketype("\nWell done! You managed to lure the bear away from the door.")
    diamond_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")

# monster room
def monster_room():
  # some prompts
  faketype("\nNow you entered the room of a monster!")
  faketype("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
  faketype("1). Go through the door silently.")
  faketype("2). Kill the monster and show your courage!")

  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the diamond_room()
    diamond_room()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The monster was hungry, he/it ate you.")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")


# diamond room
def diamond_room():
  # some prompts
  faketype("\nYou are now in a room filled with diamonds!")
  faketype("And there is a door too!")
  faketype("What would you do? (1 or 2)")
  faketype("1). Take some diamonds and go through the door.")
  faketype("2). Just go through the door.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
  elif answer == "2":
    # the player won the game
    faketype("\nNice, you're are an honest man! Congrats you win the game!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")

# function to ask play again or not
def play_again():
  faketype("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


    # game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  faketype("\n" + reason)
  faketype("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()


# start the game
start()





