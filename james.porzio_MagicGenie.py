#Import random functions from random module to create random fortunes
import random
#import pygame for sound effects
import pygame
# initialize pygame 
pygame.init()
# load wishgrantedagain sound file
sound_file = "wishgrantedagain.wav"
# pygame mixer
mysound = pygame.mixer.Sound(sound_file)
# define new function to play the sound
def play_mysound():
    mysound.play()
#Create "inventory" of possible genie responses
inventory = ["I will grant your wish eventually, just give it some time...", "I absolutely cannot grant that wish right now, I apologize, try again another time...", "Your wish will come true with time... patience is key...", "Your wish is not possible at this moment, give it time and try again later..."]
# Print explanation for user
print("Wish for something and the Magic Genie will tell you if they can grant your wish!")
# print directions for user
print("1. Choose 1 to wish for something from the Magic Genie!")
# Ask the user to type 1 to start game, store response in "choice"
choice = input("Please type 1 here: ")
# if the user choice is 1 start the game and ask for wish
if choice == "1":
# ask for wish from user
    question = input("Your wish: ")
# user will get random genie response either granting or denying wish
    FortuneNumber = random.randint(0, len(inventory) - 1)
# print magic genie response
    print(inventory[FortuneNumber])
# play sound during genie response
    play_mysound()
# text response for invalid user input
else:
    print("That is not correct. Please stop.")
