# Written by Justice V

'''
# Question 1
# Ask the user for two integers
larger = int(input("Enter the larger number: "))
smaller = int(input("Enter the smaller number: "))

# Count how many times larger can be halved while still greater than smaller
count = 0
current = larger

while current > smaller:
    current /= 2
    if current > smaller:
        count += 1

print("Larger can be halved", count, "times while still being greater than smaller.")
'''
'''
# Question 2

user_word = input("Enter a word: ")

# Print every other letter starting with the second letter (index 1)
for i in range(1, len(user_word), 2):
    print(user_word[i], end=' ')
'''
'''
# Question 3

number = 37

while number <= 1050:
    if number % 2 == 0:
        print(number, end=' ')
    number += 1
'''
'''
# Question 4

total = ''
user_input = ''
done = False

while not done:
    user_input = input("Enter a letter to create a word: ")
    if user_input.lower() == 'done':
        done = True
    else:
        total += user_input + ''

print(f'Your word is: {total}')
'''
'''
# Question 5

total = 0
number = 50

while number <= 517:
    if number % 2 == 1:
        total += number
    number += 1

print("The sum of all odd numbers from 50 to 517 is:", total)
'''
'''
# Question 6

total = 0
user_input = ''
done = False

while not done:
    user_input = int(input("Enter a number: "))
    if user_input  < 0:
        done = True
    else:
        total += user_input 

print(total)
'''
'''
# Question 7

# Hailstone sequence starting at n = 25

n = 25
print("Hailstone sequence starting at", n, ":")

while n != 1:
    print(n, end=" ")
    if n % 2 == 0:   # if n is even
        n = n // 2
    else:            # if n is odd
        n = 3 * n + 1

print(1)  # finally print the last 1
'''
'''
# Question 8

num = 1
user_input = int(input("Enter Number: "))

print(f"Factors up to {user_input}:")
while num <= user_input:
    if user_input % num == 0:
        print(num, end=' ')
    num += 1
print()
'''
'''
# Question 9

width = int(input("Enter width: "))
height = int(input("Enter height: "))
pattern = input("Enter pattern: ")
row = 0
while row < height:
    column = 0
    while column < width:
        print(pattern, end='')
        column += 1
    print()  # Move to the next line after each row
    row += 1
'''
'''
# Question 10

largest_even = -1  # start with -1 in case no even numbers are entered

while True:
    num = int(input("Enter an integer (negative to stop): "))
    
    if num < 0:
        break  # stop when a negative number is entered
    
    if num % 2 == 0 and num > largest_even:
        largest_even = num

print("The largest even number entered is:", largest_even)
'''

# Question 11

# Ask the user for an integer
n = int(input("Enter a positive integer: "))

# Calculate the sum of squares up to n
total = 0
for i in range(1, n + 1):
    total += i * i   # same as i**2

print("The sum of squares up to", n, "is:", total)

