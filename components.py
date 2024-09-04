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
    (10**33, "decillion")
    ]
    # Determine the magnitude of the number and return its most significant part
    if(number >= 1E36):
        power_of_ten = len(str(number)) - 1
        most_significant_part  = number // 10 ** power_of_ten
        word_representation = f"{most_significant_part}E{str(power_of_ten)}"
        print(f"Word Representation: {word_representation}")
    elif(number >= 1E3): 
        for magnitude, name in reversed(magnitudes):
            if number >= magnitude:
                most_significant_part  = number // magnitude
                word_representation = f"{most_significant_part} {name}"
                break # Exit the loop once the magnitude is found
    else:
        word_representation = f"{number}" # If the number is less than 1000 write it the same way
    return word_representation

def check_length_after_decimal(number):
    number_str = str(number)
    # Check if there is a decimal point in the string
    if 'E-'in number_str:
        # Split the string at the decimal point and count the length of the part after it
        length_after_decimal = int(number_str.split('E-')[1])
    elif '.' in number_str:
        # Split the string at the decimal point and count the length of the part after it
        length_after_decimal = len(number_str.split('.')[1])
    else:
        length_after_decimal =  0
    return length_after_decimal
