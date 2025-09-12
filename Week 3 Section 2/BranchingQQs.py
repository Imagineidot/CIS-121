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

