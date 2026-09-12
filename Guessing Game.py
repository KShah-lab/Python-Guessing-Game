import random
import pygame
import colorama
from colorama import Fore, Style

ORANGE = "\033[38;5;208m"

print(ORANGE + "====================================" + Style.RESET_ALL)
print(ORANGE + "        NUMBER GUESSING GAME        " + Style.RESET_ALL)
print(ORANGE + "====================================" + Style.RESET_ALL)
print(ORANGE + "          👉 by Khaleeq  👈             " + Style.RESET_ALL)
print(ORANGE + "====================================" + Style.RESET_ALL)

pygame.mixer.init()

well_done_sound = pygame.mixer.Sound("Well done.mp3")
wrong_sound = pygame.mixer.Sound("Lose.mp3")
game_over_sound = pygame.mixer.Sound("Lose2.mp3")

num = random.randint(1, 150)
print("Python has selected a number between 1 and 150. Now it's your turn!")

lives = 8

while lives > 0:
    guess = int(input("Enter the number you guessed = "))

    if guess == num:
        print(Fore.LIGHTGREEN_EX + "Well done! You guessed the correct number!" + Style.RESET_ALL)
        well_done_sound.play()
        break

    elif guess < num:
        print(Fore.RED + "It's a bigger number!" + Style.RESET_ALL)
        wrong_sound.play()
        lives -= 1

    elif guess > num:
        print(Fore.RED + "It's a smaller number!" + Style.RESET_ALL)
        wrong_sound.play()
        lives -= 1

    print("Number of lives:", lives)

if lives == 0:
    print(Fore.LIGHTRED_EX + "Game Over! Restart to play again!" + Style.RESET_ALL)
    game_over_sound.play()

    
#I am doing mostly a trial and error process of trying to get a fixed number of lives, but they go down if you guess the number wrong\
#I also want to try add sounds so that when you lose it makes a sad sound with GAME OVER but when you win, it says WELL DONE!
#I am watching and learning a couple of tutorials that will teach me how to do the above feature.