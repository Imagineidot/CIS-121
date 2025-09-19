# Written by Justice V

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
