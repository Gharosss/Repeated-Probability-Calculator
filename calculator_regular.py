from fractions import Fraction
from decimal import Decimal, getcontext
from components import *


# Calculate the chance of occurence for values that are larger than 1E-16
def calculate_regular_chances(occurence_chance, target_percentage):
    
    # Convert the number to a string
    getcontext().prec = max(check_length_after_decimal(occurence_chance) + 5, 5)
    
    target_probability=Fraction(target_percentage, 100)
    scientific_version = False
    if occurence_chance < 0: 
        scientific_version = True
        occurence_chance *= -1
        
    # Convert to Decimal for high-precision calculations
    occurence_chance_decimal = Decimal(occurence_chance)
    target_prob_decimal = Decimal(target_probability.numerator) / Decimal(target_probability.denominator)

    num_of_tries = ((1 - target_prob_decimal).ln() / (1 - occurence_chance_decimal).ln()).quantize(Decimal(1), rounding='ROUND_CEILING')
    final_probability = 1 - (1 - occurence_chance) ** num_of_tries
    
    if(scientific_version):
        num_of_tries_display = f"{num_of_tries:,}"
        final_probability_display = final_probability
    else:
        num_of_tries_display = represent_in_words(num_of_tries)
        final_probability_display = f"{final_probability:.3f}"
        
    print(f"After {colors.CYAN}{num_of_tries_display} tries{colors.RESET}, the chance of occurence is {colors.CYAN}{final_probability_display}{colors.RESET}\n")
    return