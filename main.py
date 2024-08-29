import math
from decimal import Decimal

class colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def represent_in_words(number):
    magnitudes = [
    (10**3, "thousand"),
    (10**6, "million"),
    (10**9, "billion"),
    (10**12, "trillion"),
    (10**15, "quadrillion"),
    (10**18, "quintillion"),
    (10**21, "sextillion"),
    (10**24, "septillion"),
    (10**27, "octillion"),
    (10**30, "nonillion"),
    ]
    
    if(number > 1000):
        for magnitude, name in magnitudes:
            if number >= magnitude:
                most_significant_part  = number // magnitude
                word_representation = f"{most_significant_part} {name}"
    else:
        word_representation = f"{number:,}"
    return word_representation

def calculate(occurence_chance):
    scientific_version = False
    if (occurence_chance < 0):
        scientific_version = True
        occurence_chance *= -1
    
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
        
        jump_size_display = represent_in_words(jump_size_guesstimate)
        if(scientific_version):
            num_of_tries_display = f"{num_of_tries:,}"
            occurence_chance_after_tries_display = occurence_chance_after_tries
        else:
            num_of_tries_display = represent_in_words(num_of_tries)
            occurence_chance_after_tries_display = f"{occurence_chance_after_tries:.3f}"
            
        if(occurence_chance_after_tries == 0):
            print("The probability is too low to calculate. PLease enter a value higher than 5E-29")
            return
        
        difference = Decimal(0.5) - occurence_chance_after_tries
        
        calculation_steps += 1
        print(f"{calculation_steps}. step's jump size is {colors.BLUE}{jump_size_display}{colors.RESET}")
        print(f"After {colors.CYAN}{num_of_tries_display} tries{colors.RESET}, the chance of occurence is {colors.CYAN}{occurence_chance_after_tries_display}{colors.RESET}")
        jump_size_guesstimate = math.floor((difference/occurence_chance)*Decimal(1.5))
        
        if(float(occurence_chance_after_tries_display) >= 0.5 and not scientific_version):
            print(f"It becomes probable after {colors.GREEN}{num_of_tries_display} tries{colors.RESET}")
            return
            
        
    print_answer(num_of_tries) 
    return

def print_answer(this_many_tries):
    if(this_many_tries != 1):
        print(f"It becomes probable after {colors.GREEN}{this_many_tries:,} tries{colors.RESET}")
    else:
        print(f"It becomes probable after {colors.GREEN}1 try{colors.RESET}") 
    
while(True):
    try:
        occurence_chance = Decimal((input("Please enter the event probability, ranging from 0 to 1, start with \"-\" for the scientific version\n")))
        if(occurence_chance <= 1 and occurence_chance >= -1):
            calculate(occurence_chance)
    except:
        print("Invalid input.")
