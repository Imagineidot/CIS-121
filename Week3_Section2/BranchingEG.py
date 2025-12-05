# Written by Justice V.

age = int(input('Enter your age: '))
status = input("What's your Status: ")
'''
if age < 3:
    print('Price = Free')
else:
    if age < 18:
        print('Price = $10')
    else:
        if age > 65:
            print('Price = $15')
        else:
            if status == 'military'
                print('Price = $16')
            else:
                if status == 'student"
                    print('Price = 16')
                else:
                    print('Price = $20')
            '''

# Condense Using elif statements instead of else and if

if age < 3:
    print('Price = Free')
elif age < 18:
    print("Price = $10")
elif age > 65:
    print("Price = $15")
    if status == 'military':
        print("New Price = $10")
elif status == 'military':
    print("Price = $16")
elif status == 'student':
    print("Price = $16")
else:
    print('Price = $20')