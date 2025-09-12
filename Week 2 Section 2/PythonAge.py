# Written by Justice V.

import math

# Part 1 (Dog Years)

# A. Write code that takes human years to dog years
'''
human_years = float(input("Enter Human Age: "))
dog_years = 7 * human_years 

print(f'You are {dog_years} years old in dog years')
'''

# B. Modify so it reports Years, Months, and Days

human_years = float(input("Enter Human Age: "))
dog_years = 7 * human_years 
years = int(dog_years)
dog_months = (dog_years - years) * 12
months = int(dog_months)
days = int((dog_months - months) * 30) 

print(f'your age in dogs years is {years} years, {months} months, {days} days. ')

'''
# Part 2 (Cat Years)

# Part A

human_years = float(input("Enter Human Age: "))
cat_years = human_years / 9 

print(f'You are {cat_years} years old in cat years')
'''

# B. Modify so it reports Years, Months, and Days

#human_years = float(input("Enter Human Age: "))
cat_years = human_years / 9 
years = int(cat_years)
cat_months = (cat_years - years) * 12
months = int(cat_months)
days = int((cat_months - months) * 30) 

print(f'your age in cat years is {years} years, {months} months, {days} days. ')

'''
# Part 3 (Horse Years)

# Part A

human_years = float(input("Enter Human Age: "))
horse_years = 3*(((human_years)**2 - 47)/7 + 12)

print(f'You are {horse_years} years old in horse years')
'''

# B. Modify so it reports Years, Months, and Days

#human_years = float(input("Enter Human Age: "))
horse_years = 3*(((human_years)**2 - 47)/7 + 12)
years = int(horse_years)
horse_months = (horse_years - years) * 12
months = int(horse_months)
days = int((horse_months - months) * 30) 

print(f'your age in horse years is {years} years, {months} months, {days} days. ')
