from calculator_regular import calculate_regular_chances
from decimal import Decimal

# Main loop to accept user input and perform calculations
while(True):
        occurence_chance = Decimal((input("Please enter the event probability, ranging from 0 to 1, start with \"-\" for the scientific version.\n")))
        if(occurence_chance > 1 or occurence_chance < -1):
            print("The probability can not be higher than 100%.")
            continue
        if(occurence_chance == 0):
            print("It is impossible for the event to occur.")
            continue
        #target_percentage = int((input("Please enter the target likelihood percentage.\n")))
        
        
        
        if(occurence_chance >= Decimal("5E-29")):
            calculate_regular_chances(occurence_chance, 30)
            continue
        else:
            print("The probability given is too small to calculate.")