import math
from decimal import Decimal
from fractions import Fraction
from components import *

def _estimate_jump_size(occurence_chance, difference, target_probability): # Used in the older version of the calculation, Redundant
    # A coefficient for the step size estimation. Higher values decrease the number of steps it takes to reach the target probability but may lead to overshooting.
    ESTIMATION_COEFFICIENT = Decimal(1.5) # Recommended value is 1.35 as no overshooting was observed when target probability is 0.5.
    
    jump_size_estimate = math.floor((difference/occurence_chance) * ESTIMATION_COEFFICIENT * target_probability**2)
    
    # jump_size_estimate =  math.floor(math.log2(1 / (difference + occurence_chance))) * 10
    
    return max(jump_size_estimate, 1)

def calculate_approaching(occurence_chance, target_percentage): # An older and slower version, Redundant
    """
    Calculates the number of tries needed for an event with a given probability to become probable (chance ≥ 50%).
    
    Parameters:
    occurence_chance (Decimal): The probability of an event occurring, ranging from 0 to 1. If negative, it triggers scientific mode.
    
    This function prints intermediate steps and results, including the calculated number of tries and the probability.
    """
    
    LOWER_PROBABILITY_LIMIT = "5E-29" # The minimum probability that can be calculated with the current version of the method.
    TOLERANCE = Decimal("1E-10")  # Tolerance value to handle precision issues
    target_probability=Fraction(target_percentage, 100)
    scientific_version = False
    if occurence_chance < 0: 
        scientific_version = True
        occurence_chance *= -1
    
    # Convert Fraction to Decimal for printing and comparisons
    target_probability_decimal = Decimal(target_probability.numerator) / Decimal(target_probability.denominator)
    
    print(f"\nAfter {colors.CYAN}each try{colors.RESET}, the chance of occurence is {colors.CYAN}{occurence_chance}{colors.RESET}\n")
    chance_of_not_occuring = 1 - occurence_chance
    current_prob = occurence_chance
    num_of_tries = 1
    calculation_steps = 0

    # Initial estimate for jump size
    jump_size_estimate = _estimate_jump_size(occurence_chance, target_probability_decimal - current_prob, target_probability_decimal)
    
    while current_prob < target_probability_decimal:
        
        # Update number of tries needed by adding the jump size
        num_of_tries += int(jump_size_estimate)
        remaining_prob = Decimal(chance_of_not_occuring) ** num_of_tries
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
        if current_prob < TOLERANCE:
            print(f"The probability is too low to calculate. Please enter a value higher than {LOWER_PROBABILITY_LIMIT}")
            return
        
        difference = target_probability_decimal - current_prob
        
        calculation_steps += 1
        print(f"{calculation_steps}. step's jump size is {colors.BLUE}{jump_size_display}{colors.RESET}")
        print(f"After {colors.CYAN}{num_of_tries_display} tries{colors.RESET}, the chance of occurence is {colors.CYAN}{current_prob_display}{colors.RESET}\n")
        
        # Adjust the jump size for the next iteration
        jump_size_estimate = _estimate_jump_size(occurence_chance, difference, target_probability_decimal)
        
         # On the non-scientific version, stops further calculations after the rounded probability is more than or equal to the target probability
        if(float(current_prob_display) >= target_probability and not scientific_version):
            print(f"It becomes probable after {colors.GREEN}{num_of_tries_display} tries{colors.RESET}")
            return
        
    if(num_of_tries != 1):
        print(f"It becomes probable after {colors.GREEN}{num_of_tries:,} tries{colors.RESET}")
        return
    else:
        print(f"It becomes probable after {colors.GREEN}1 try{colors.RESET}") 
        return