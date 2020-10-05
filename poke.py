import random
import sys
import time

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
        
# The Random Genorated Names of pokemon
#------------------------------------------------------------------------------

first = ["Gli", "Gar", "Giga", "Hy", "Dragon", "De", "Medi",
         "Fly", "Shell", "Pory", "Zig", "Pidge"]
second = ["gar", "scor", "chomp", "gon", "nite", "itite"
          "bador", "dreigon", "drago", "enne", "lil", "cham",
          "tail", "goon" ]

pokemon = [] # empty array

for i in range(1000): # Will always have over 151 items within the list
    name1 = random.choice(first)
    name2 = random.choice(second)
    poke = name1+name2
    pokemon.append(poke)

# remove dups of the list
pokemon = list(dict.fromkeys(pokemon))
print(pokemon,"\n", "\nThe amount of pokemon in the list is", len(pokemon))

#------------------------------------------------------------------------------

delay_print("Welcome to the pokemon battle simulator") # slow typing affect similar to the actual game
delay_print("\nI am professor Oak and I know you have the ability to become a great pokemon trainer")

class Pokemon:
    def __init__(self, name):
        self.name = name

    def fight(self, Pokemon2):
        # Pokemon Single battle
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
