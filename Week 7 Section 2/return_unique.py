# Wirtten  by Justice V.

"""
Each number repeats at least once, except for two. Return the two unique numbers.
"""
from collections import Counter

def return_unique(numbers):
    counts = Counter(numbers)
    uniques = [x for x, c in counts.items() if c == 1]
    if len(uniques) != 2:
        raise ValueError("Expected exactly two unique elements")
    return uniques

if __name__ == "__main__":
    user_input = input("Enter a array of numbers separated by commas that has to be two unique numbers: ")
    number_list = [int(num.strip()) for num in user_input.split(",")]
    print(return_unique(number_list))
   # print(return_unique([1,9,8,8,7,6,1,6]))                       # [9, 7]
   # print(return_unique([5,5,2,4,4,4,9,9,9,1]))                   # [2, 1]
   # print(return_unique([9,5,6,8,7,7,1,1,1,1,1,9,8]))             # [5, 6]
