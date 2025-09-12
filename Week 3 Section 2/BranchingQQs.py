# Written by Justice V.

# Question 1

my_var = int(input('Variable: '))

if my_var % 2 == 1:
    if my_var **3 != 27:
        my_var = my_var +4 #Assignment 1 (5)
    else:
        my_var /= 1.5 #Assignment 2 (3)
else:
    if my_var <= 10:
        my_var *= 2 #Assignment 3 (6)
    else:
        my_var -= 2 #Assignment 4 (12)
print ( my_var )

