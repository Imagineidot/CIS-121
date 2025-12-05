# Wirtten  by Justice V.

def return_unique(numbers):
    counts = {}
    for x in numbers:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    result = []
    for x in counts:
        if counts[x] == 1:
            result.append(x)

    if len(result) == 2:
        print(result[0], result[1])
    else:
        print("Did not find exactly two unique numbers.")

if __name__ == "__main__":
    raw = input("Enter integers (space-separated): ")
    nums = []
    for part in raw.split():
        nums.append(int(part))
    return_unique(nums)
