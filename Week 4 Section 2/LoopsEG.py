# Written by Justice V

# LOOPS

'''
# Print numbers 1 to 10 using a while loop
number = 1

while number <= 10:
    print(number)
    number += 1
'''
'''
# Print even numbers from 1 to 10 using a while loop
number = 2

while number <= 10:
    print(number, end=' ')
    number += 2
'''
'''
number = 1
while number <= 10:
    
        print(number, end=' ')
    number += 1
'''
'''
number = int(input("enter number <=10: "))
while number <= 10:
    if number % 2 == 1:
        number += 1
    print(number, end=' ')
'''
'''
# Print all odd numbers between 5 and some number given by the user
end = int(input("Enter a number greater than 5: "))
start = 5
while start <= end: # Keeps going until its not <= end(EG: end = 15, it goes 5-15 (5,6,...,15) every number between)
    if start % 2 == 1:
        print(start)
    start += 1
'''
'''
# Print all even numbers not divisible by 3

number = 0
    
while number < 50:
    number += 1
    if number % 2 == 0:
        if number % 3 == 0:
            continue
        print(number, end=' ')
number = 0
'''
'''
# Write a program that adds numbers until the user says stop

total = 0

user_num = input("Enter a number or type q to end: ")

while user_num != 'q':
    total += int(user_num)
    user_num = input("Enter a number or type q to end: ")
 
print(f'total = {total}')
'''

total = 0
user_num = ''
done = False

while not done:
    user_num = input("Enter a number or type q to end: ")
    if user_num != 'q':
        total += int(user_num)
    else:
        done = True

print(f'total = {total}')

total = 0
user_num = ''
done = False

while True:
    user_num = input("Enter a number or type q to end: ")
    if user_num != 'q':
        total += int(user_num)
    else:
        break

print(f'total = {total}')
