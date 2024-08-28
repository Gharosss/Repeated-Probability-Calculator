import math
from decimal import Decimal

class colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def calculate(occurence_chance):
    print(f"After {colors.CYAN}1 try{colors.RESET}, the chance of occurence is {colors.CYAN}{occurence_chance}{colors.RESET}")
    chance_of_not_occuring = 1 - occurence_chance
    not_occurence_chance_after_tries = 1 - occurence_chance
    num_of_tries = 1
    calculation_steps = 0
    
    
    jump_size_guesstimate = math.floor(1/occurence_chance/2)
    
    while(not_occurence_chance_after_tries > 0.5):
        if (jump_size_guesstimate < 1):
            jump_size_guesstimate = 1
        num_of_tries += jump_size_guesstimate
        not_occurence_chance_after_tries = chance_of_not_occuring**num_of_tries
        occurence_chance_after_tries = 1 - not_occurence_chance_after_tries
        
        if(occurence_chance_after_tries == 0):
            return -1
        
        difference = Decimal(0.5) - occurence_chance_after_tries
        
        calculation_steps += 1
        print(f"{calculation_steps}. step's jump size was {colors.BLUE}{jump_size_guesstimate:,}{colors.RESET}")
        print(f"After {colors.CYAN}{num_of_tries:,} tries{colors.RESET}, the chance of occurence is {colors.CYAN}{occurence_chance_after_tries}{colors.RESET}")
        jump_size_guesstimate = math.floor((difference/occurence_chance)*Decimal(1.5))
        
    return num_of_tries

def print_answer(this_many_tries):
    if(this_many_tries != 1):
        print(f"It becomes probable after {colors.GREEN}{this_many_tries} tries{colors.RESET}")
    else:
        print(f"It becomes probable after {colors.GREEN}1 try{colors.RESET}") 
    
while(True):
        occurence_chance = Decimal((input("Please enter the event probability, ranging from 0 to 1 \n")))
        if(occurence_chance <= 1 and occurence_chance > 0):
            this_many_tries = calculate(occurence_chance)
            if(this_many_tries == -1):
                print("The probability is too low to calculate")
            else:
                print_answer(this_many_tries)

