import random

def deranged_shuffle(lst):
    while True:
        shuffled = lst[:]
        random.SystemRandom().shuffle(shuffled)
        if all(a != b for a, b in zip(lst, shuffled)):
            return shuffled
original = [1, 2, 3, 4, 5]
shuffled = deranged_shuffle(original)

print("Original:", original)
print("Shuffled (deranged):", shuffled)
