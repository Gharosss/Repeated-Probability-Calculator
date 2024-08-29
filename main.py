import math
from decimal import Decimal

# A class to store ANSI escape codes for colored terminal text output.
class colors: 
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

#Converts a large number into a human-readable format using magnitude suffixes (e.g., thousand, million).
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
    
    # Determine the magnitude of the number and return its most significant part
    if(number > 1000): 
        for magnitude, name in reversed(magnitudes):
            if number >= magnitude:
                most_significant_part  = number // magnitude
                word_representation = f"{most_significant_part} {name}"
                break # Exit the loop once the magnitude is found
    else:
        word_representation = f"{number}" # If the number is less than 1000 write it the same way
    return word_representation

def calculate(occurence_chance, target_probability = Decimal(0.5)):
    """
    Calculates the number of tries needed for an event with a given probability to become probable (chance ≥ 50%).

    Parameters:
    occurence_chance (Decimal): The probability of an event occurring, ranging from 0 to 1. If negative, it triggers scientific mode.

    This function prints intermediate steps and results, including the calculated number of tries and the probability.
    """
    # The minimum probability that can be calculated with the current version of the method.
    LOWER_PROBABILITY_LIMIT = "5E-29" 
    # A coefficient for the step size estimation. Higher values decrease the number of steps it takes to reach the target probability but may lead to overshooting.
    ESTIMATION_COEFFICIENT = Decimal(1.5) # Recommended value is 1.5 as no overshooting was observed when target probability is 0.5.
    
    scientific_version = False
    # Detect scientific version based on negative probability input and convert it back to a positive value
    if (occurence_chance < 0):
        scientific_version = True
        occurence_chance *= -1 
    
    print(f"\nAfter {colors.CYAN}each try{colors.RESET}, the chance of occurence is {colors.CYAN}{occurence_chance}{colors.RESET}\n")
    chance_of_not_occuring = 1 - occurence_chance
    current_prob = occurence_chance
    num_of_tries = 1
    calculation_steps = 0
    difference = target_probability - occurence_chance
    
    # Initial guess for jump size in number of tries
    jump_size_estimate = math.floor(1/occurence_chance/2)
    
    # Loop until the probability of occurrence after many tries becomes greater than or equal to the target probability
    while(current_prob < target_probability):
        if (jump_size_estimate < 1): # This prevents the guesstimate to get smaller than 1 in the final steps
            jump_size_estimate = 1
        
        # Update number of tries needed by adding the jump size
        num_of_tries += jump_size_estimate
        remaining_prob = chance_of_not_occuring**num_of_tries
        current_prob = 1 - remaining_prob
        
        # Display options for normal and scientific versions
        jump_size_display = represent_in_words(jump_size_estimate)
        if(scientific_version):
            num_of_tries_display = f"{num_of_tries:,}"
            current_prob_display = current_prob
        else:
            num_of_tries_display = represent_in_words(num_of_tries)
            current_prob_display = f"{current_prob:.3f}"
        
        # Check for incalculably low probabilities
        if(current_prob == 0):
            print(f"The probability is too low to calculate. PLease enter a value higher than {LOWER_PROBABILITY_LIMIT}")
            return
        
         # Calculate the difference from the target probability of 50%
        difference = target_probability - current_prob
        
        calculation_steps += 1
        print(f"{calculation_steps}. step's jump size is {colors.BLUE}{jump_size_display}{colors.RESET}")
        print(f"After {colors.CYAN}{num_of_tries_display} tries{colors.RESET}, the chance of occurence is {colors.CYAN}{current_prob_display}{colors.RESET}\n")
        print(remaining_prob)
        # Adjust the jump size for the next iteration
        jump_size_estimate = math.floor((difference/occurence_chance) * ESTIMATION_COEFFICIENT)
        
        # On the non-scientific version, stops further calculations after the rounded probability is more than or equal to the target probability
        if(float(current_prob_display) >= target_probability and not scientific_version):
            print(f"It becomes probable after {colors.GREEN}{num_of_tries_display} tries{colors.RESET}")
            return
            
    # Print the final result once the loop terminates
    print_answer(num_of_tries) 
    return

# Prints the result, indicating the number of tries needed for the event to become probable.
def print_answer(this_many_tries):
    if(this_many_tries != 1):
        print(f"It becomes probable after {colors.GREEN}{this_many_tries:,} tries{colors.RESET}")
    else:
        print(f"It becomes probable after {colors.GREEN}1 try{colors.RESET}") 
    
# Main loop to accept user input and perform calculations
while(True):
    # try:
        # Accept user input as a probability value between 0 and 1 (or negative for scientific version)
        occurence_chance = Decimal((input("Please enter the event probability, ranging from 0 to 1, start with \"-\" for the scientific version\n")))
        if(occurence_chance <= 1 and occurence_chance >= -1 and occurence_chance != 0):
            calculate(occurence_chance)
    # except:
    #     print("Invalid input.")
