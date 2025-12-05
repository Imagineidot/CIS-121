# Written by Justice V.

# Question 1 (Heads or Tails)
'''
def  toss_coin(guess = 0):
    from random import randint
    guess = int(input("Type 0 for Heads or 1 for Tails. Default is Heads. ") or guess)
    value = randint(0,1)
    print("Coin landed on: ", "Heads" if value == 0 else "Tails")
    print("Correct" if guess==value else "Incorrect")

# Run Function For Testing
toss_coin()
'''
'''
# Question 2 (Odd or Even)

def guess(guess = "even"):
    from random import randint
    guess = input("Enter Odd or Even: ") or guess
    value = randint(0,9)
    print("Number:", value)
    is_even = (value % 2 == 0)
    user_even = (guess.strip().lower()== "even")
    print("Correct!" if (is_even == user_even) else "Incorrect!")

# Run Function for Testing
guess()
'''
'''
# Question 3 (Count Duplicates)

def count_duplicates(n1 = 0, n2 = 0, n3 = 0):
    n1 = int(input("Enter n1: ") or n1)
    n2 = int(input("Enter n2: ") or n2)
    n3 = int(input("Enter n3: ") or n3)
    
    if n1 == n2 and n1 == n3 and n2 == n3:
        print("There are three of the same numbers. ")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("There are two of the same numbers. ")
    else:
        print("Each number is unique. ")    
    
# Run Function for Testing
count_duplicates()
'''
'''
# Question 4 (Rock Paper Scissors)

def find_winner(p1 = "Rock", p2 = "Rock"):
    p1 = input("Player 1 Enter Rock, Paper, or Scissors: ") or p1
    p2 = input("PLayer 2 Enter Rock, Paper, or Scissors: ") or p2
    p1 = p1.strip().lower()
    p2 = p2.strip().lower()
    
    if p1 == p2:
        print("It's a Tie! ")
    elif (p1, p2) in {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}:
        print("Player 1 Wins! ")
    else:
        print("Player 2 Wins!")

# Run Function for Testing
find_winner()
'''
'''
# Question 5 (Luke's Relations)

def find_relation(name = ""):
    name = input("Enter your name for relationship status: ").strip().lower()
    rel = {
        "darth vader": "Father",
        "leia": "Sister",
        "han": "Brother in Law",
        "r2d2": "Droid"
    }
    print("Relationship:", rel.get(name.strip().lower(), "Unknown"))

# Run Function for Testing
find_relation()
'''
'''
# Question  6 (Hailstone Sequence)

def hailstone_seq(n = 40):
    n = int(input("Enter Number: ") or n)
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    print(seq)

# Run Function for Testing
hailstone_seq()
'''
'''
# Question 7 (Ascending Order)

def ascending_order(n1 = None, n2 = 5, n3 = 25):
    if n1 is None:
        n1 = int(input("Enter First Number "))
    else:
        n1 = int(n1)
    n2 = int(input("Enter Second Number ") or n2)
    n3 = int(input("Enter Third Number: ") or n3)
    if n1 > n2: 
        n1, n2 = n2, n1
    if n2 > n3: 
        n2, n3 = n3, n2
    if n1 > n2: 
        n1, n2 = n2, n1
    print([n1, n2, n3])

# Run Function for Testing
ascending_order()
'''
'''
# Question 8 (Descending Order)

def descending_order(n1 = None, n2 = 15, n3 = 5):
    if n1 is None:
        n1 = int(input("Enter First Number: "))
    else:
        n1 = int(n1)
    n2 = int(input("Enter Second Number: ") or n2)
    n3 = int(input("Enter Third Number: ") or n3)
    if n1 < n2:
        n1, n2 = n2, n1
    if n2 < n3:
        n2, n3 = n3, n2
    if n1 < n2:
        n1, n2 = n2, n1
    print([n1,n2,n3])

# Run Function for Testing
descending_order()
'''
'''
# Question 9 (Indices of a Value)

def get_indices(lst = None, value = 0):
    if lst is None:
        lst = input("Enter List Elements Seperated by Commas: ").split(",")
    value = input("Enter Value to Search for: ") or value
    idx = [i for i, v in enumerate(lst) if v == str(value)]
    print("indices:", idx)

# Run Function for Testing
get_indices()
'''
'''
# Question 10 (Factors)

def find_factors(n = 36):
    n = int(input("Enter a Positive Number: ") or n)
    factors = [d for d in range(1, n + 1) if n % d == 0]
    print("Factors: ", factors)

# Run Function for Testing
find_factors()
'''
'''
# Question 11 (List of Multiples)

def list_of_multiples(n = None, length = 5):
    if n is None:
        n = int(input("Enter Number To be Multiplied: "))
    length = int(input("Enter Number of multiples: ") or length)
    print([n * k for k in range(1, length + 1)])

# Run Function for Testing
list_of_multiples()
'''
'''
# Question 12 (Report Evens)

def is_evens(n):
    return n % 2 == 0

def report_evens():
    nums = list(map(int, input("Enter Numbers Seperated by Commas: ").split(",")))
    evens = [x for x in nums if is_evens(x)]
    print("Even Numbers: ", evens)

# Run Function for Testing
report_evens()
'''
'''
# Question 13 (Report Vowels)

def is_vowel(ch):
    return ch.lower() in "aeiou"

def report_vowels():
    word = input("Enter a Word: ")
    vowels = [ch for ch in word if is_vowel(ch)]
    print("Vowels: ", vowels)

# Run Function for Testing
report_vowels()
'''
'''
# Question 14 (Report Two Digit Numbers)

def is_two_digit_number(n):
    return (10<= n <= 99) or (-99 <= n <= -10)

def report_two_digit_number():
    nums = list(map(int, input("Enter Numbers Seperated by Commas: ").split(",")))
    two_digits = [x for x in nums if is_two_digit_number(x)]
    print("Two Digit Numbers: ", two_digits)
# Run Function for Testing
report_two_digit_number()
'''
'''
# Question 15 (Report Negative Odds)

def is_negative(n):
    return n < 0

def is_odd(n):
    return n % 2 != 0

def report_negative_odds():
    nums = list(map(int, input("Enter Numbers Seperated by Commas: ").split(",")))
    negative_odds = [x for x in nums if is_negative(x) and is_odd(x)]
    print("Negative Odds: ", negative_odds)

# Run Function for Testing
report_negative_odds()
'''
