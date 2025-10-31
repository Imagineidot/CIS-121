# Written by Justice V.

'''
# Question 1

def reverse_string(word):
    return word[::-1]

user_word = input("Enter a word: ")
reversed_word = reverse_string(user_word)
print(f'Reversed word: {reversed_word}')
'''
'''
# Question 2

def is_fever(temp):
    # last character tells us if it's Fahrenheit or Celsius
    unit = temp[-1]
    # everything before the last character is the number
    value = float(temp[:-1])

    if unit == "F":
        return value > 98.6
    elif unit == "C":
        return value > 37
    else:
        raise ValueError("Temperature must end with 'F' or 'C'.")

user_temp = input("Enter the temperature (e.g., 99F or 37C): ")
print(is_fever(user_temp))
'''

# Question 3

def is_boiling(temp):
    unit = temp[-1]
    value = float(temp[:-1])
    if unit == "F":
        return value >= 212
    elif unit == "C":
        return value >= 100
    else:
        raise ValueError("Temperature must end with 'F' or 'C'.")
user_temp = input("Enter the temperature (e.g., 212F or 100C): ")
print(is_boiling(user_temp))