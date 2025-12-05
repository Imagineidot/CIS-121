# Written by Justice V.

def find_unique(numbers):
    counts = {}
    for x in numbers:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    for x in counts:
        if counts[x] == 1:
            return x
    return None

if __name__ == "__main__":
    raw = input("Enter integers (space-separated): ")
    nums = []
    for part in raw.split():
        nums.append(int(part))
    print(find_unique(nums))

