# Written by Justice V.

def is_isogram(word):
    seen = {}
    for ch in word.lower():
        if ch.isalpha():
            if ch in seen:
                return False
            else:
                seen[ch] = 1
    return True

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(is_isogram(word))
