# Written by Justice V.

# Question 1
'''
my_var = int(input('Variable: '))

if my_var % 2 == 1:
    if my_var **3 != 27:
        my_var = my_var +4 #Assignment 1 (5), (Any Odd Number but 3)
    else:
        my_var /= 1.5 #Assignment 2 (3), (Only 3)
else:
    if my_var <= 10:
        my_var *= 2 #Assignment 3 (6), 
    else:
        my_var -= 2 #Assignment 4 (12), 
print ( my_var )
'''
'''
# Question 2

a). Can run both blocks if both are true
b). Can run only 1 block whichever one is true first

'''
'''
# Question 3

# Ask the user to input the light color
light_color = input("Enter the traffic light color (green, yellow, red): ").lower()

# Check the color and print the correct action
if light_color == "green":
    print("go")
elif light_color == "yellow":
    print("yield")
elif light_color == "red":
    print("stop")
else:
    print("Invalid color")
'''
'''
# Question 4

# Ask the user for their age and athleticism goal
age = int(input("Enter your age: "))
goal = input("Enter your athleticism goal (Above Average or Below Average): ").lower()

# Determine the heart rate range
if 20 <= age <= 39:
    if goal == "above average":
        print("Your resting heart rate should be between 47-72.")
    elif goal == "below average":
        print("Your resting heart rate should be between 73-93.")
    else:
        print("Invalid athleticism goal.")
elif 40 <= age <= 59:
    if goal == "above average":
        print("Your resting heart rate should be between 46-71.")
    elif goal == "below average":
        print("Your resting heart rate should be between 72-94.")
    else:
        print("Invalid athleticism goal.")
elif 60 <= age <= 79:
    if goal == "above average":
        print("Your resting heart rate should be between 45-70.")
    elif goal == "below average":
        print("Your resting heart rate should be between 71-97.")
    else:
        print("Invalid athleticism goal.")
else:
    print("Age out of supported range.")
'''
'''
# Question 5

# Prompt the user to enter three integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Use conditional logic to sort the numbers manually
if a > b:
    a, b = b, a  # Swap so that a <= b
if a > c:
    a, c = c, a  # Swap so that a <= c
if b > c:
    b, c = c, b  # Swap so that b <= c

# Now a <= b <= c
print("Numbers in increasing order:", a, b, c)
'''
'''
# Question 6

# Prompt the user to enter three integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Use conditional logic to sort the numbers manually
if a > b:
    a, b = b, a  # Swap so that a <= b
if a > c:
    a, c = c, a  # Swap so that a <= c
if b > c:
    b, c = c, b  # Swap so that b <= c

# Now a <= b <= c
print("Numbers in decreasing order:", c, b, a)
'''
'''
# Question 7

# Ask the user for an amount of knuts
knuts = int(input("Enter the amount of knuts: "))

# Conversion rates
KNUTS_PER_SICKLE = 29
SICKLES_PER_GALLEON = 17
KNUTS_PER_GALLEON = KNUTS_PER_SICKLE * SICKLES_PER_GALLEON  # 29 * 17 = 493

# Calculate galleons, sickles, and knuts
galleons = knuts // KNUTS_PER_GALLEON
remaining = knuts % KNUTS_PER_GALLEON

sickles = remaining // KNUTS_PER_SICKLE
knuts_left = remaining % KNUTS_PER_SICKLE

# Build the output string, only adding non-zero parts
output = []
if galleons > 0:
    output.append(f"{galleons} galleon{'s' if galleons > 1 else ''}")
if sickles > 0:
    output.append(f"{sickles} sickle{'s' if sickles > 1 else ''}")
if knuts_left > 0:
    output.append(f"{knuts_left} knut{'s' if knuts_left > 1 else ''}")

# Print the result
print(" ".join(output))
'''
'''
# Question 8

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))   
n3 = int(input("Enter third number: "))

if n1 > n2:
    n1, n2 = n2, n1  # Swap so that n1 <= n2
if n1 > n3:
    n1, n3 = n3, n1  # Swap so that n1 <= n3
if n2 > n3:
    n2, n3 = n3, n2  # Swap so that n2 <= n3
   
print(f'Largest Number is {n3}') 
'''
'''
# Question 9

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))   
n3 = int(input("Enter third number: "))

if n1 > n2:
    n1, n2 = n2, n1  # Swap so that n1 <= n2
if n1 > n3:
    n1, n3 = n3, n1  # Swap so that n1 <= n3
if n2 > n3:
    n2, n3 = n3, n2  # Swap so that n2 <= n3
   
print(f'Largest Number is {n1}') 
'''
'''
# Question 10

classes = input("Choose Class, Warrior, Bard, or Wizard: ").lower()
races = input("Choose Race, Elf or Ogre: ").lower()
health_points = -1

if classes == "Warrior".lower() and races == "Elf".lower():
     health_points = 150
elif classes == "Warrior".lower() and races == "Ogre".lower():
    health_points = 200
elif classes == "Bard".lower() and races == "Elf".lower():
    health_points = 75
elif classes == "Bard".lower() and races == "Ogre".lower():
    health_points = 100
elif classes == "Wizard".lower() and races == "Elf".lower():
    health_points = 25
elif classes == "Wizard".lower() and races == "Ogre".lower():
    health_points = 50
else: 
    print("Invalid Class or Race.")

print(f'You have {health_points} health points.')
'''
'''
# Question 11

from random import randint
value = randint(0, 1) # Picks a random number integer. Either 0 or 1

guess = int(input("Enter 0 for heads or 1 for tails: "))

print(f'Computer chose {value}.')
if guess == value:
    print("You win!")
else: 
    print("You lose!")
'''
'''
# Question 12

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: ")) 
n3 = int(input("Enter third number: "))

if n1 != n2 and n1 != n3 and n2 != n3:
    print("All numbers are unique.")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("You entered a duplicate number.")
'''
'''
# Question 13 

highway = int(input("Enter highway number: "))
invalids = [100, 200, 300, 400, 500, 600, 700, 800, 900]

if highway % 2 == 0 and highway not in invalids:
    print(f"Highway {highway} runs east/west.")
if highway % 2 == 1:
    print(f"Highway {highway} runs north/south.")
if highway in invalids:
    print(f"Highway {highway} is not a valid highway number.")
'''
'''
# Question 14 

vowels = ["a", "e", "i", "o", "u"]
letter = input("Enter a lowercase letter: ")

if letter in vowels:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")
'''
'''
# Question 15

grade = input("Enter your grade level: ")
time = input("Enter Morning or Afternoon: ")

if grade in ["k", "1", "2", "3"]: 
    if time == "Morning".lower():
        print("Pool is open at 9 AM.")
    elif time == "Afternoon".lower():
        print("Pool is open at 1 PM.")
elif grade in ["4", "5", "6", "7", "8"]:
    if time == "Morning".lower():
        print("Pool is open at 10 AM.")
    elif time == "Afternoon".lower():
        print("Pool is open at 2 PM.")
elif grade in ["9", "10", "11", "12"]:
    if time == "Morning".lower():
        print("Pool is open at 11 AM.")
    elif time == "Afternoon".lower():
        print("Pool is open at 3 PM.")
'''
'''
# Question 16

flavor = input("Enter ice cream flavor: ")

if flavor in ["vanilla", "chocolate", "strawberry"]:
    print(f"Here is your {flavor} ice cream!")
if flavor not in ["vanilla", "chocolate", "strawberry"]:
    print(f"Sorry, we don't have {flavor} ice cream.")
'''
'''
# Question 17

player1 = input("Enter Player 1's choice (rock, paper, or scissors): ")
player2 = input("Enter Player 2's choice (rock, paper, or scissors): ")

if player1 == "Rock".lower() and player2 == "Scissors".lower():
    print("Player 1 wins!")
elif player1 == "Rock".lower() and player2 == "Paper".lower():
    print("Player 2 wins!")
if player1 == "Scissors".lower() and player2 == "Rock".lower():
    print("Player 2 wins!")
elif player1 == "Scissors".lower() and player2 == "Paper".lower():
    print("Player 1 wins!")
if player1 == "Paper".lower() and player2 == "Rock".lower():
    print("Player 1 wins!") 
elif player1 == "Paper".lower() and player2 == "Scissors".lower():
    print("Player 2 wins!")
'''
'''
# Question 18

length1 = float(input("Enter length of side 1: "))
length2 = float(input("Enter length of side 2: "))
length3 = float(input("Enter length of side 3: "))

if length1 != length2 and length1 != length3 and length2 != length3:
    print("scalene triangle")
elif length1 == length2 and length1 == length3 and length2 == length3:
    print("equilateral triangle")
elif length1 == length2 or length1 == length3 or length2 == length3:
    print("isosceles triangle")
'''
'''
# Question 19

luke = (input("Enter someones name:"))

if luke == "Darth Vader".lower():
    print("Relation: Father")
elif luke == "Leia".lower():
    print("Relation: Sister")
elif luke == "Han".lower():
    print("Relation: Brother in Law")
elif luke == "R2D2".lower():
    print("Relation: Droid")
else:
    print("Relation: Unknown")
'''