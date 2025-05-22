from itertools import combinations

def split_min_diff(lst):
    n = len(lst)
    if n < 2:
        return lst, []

    best_diff = float('inf')
    best_pair = ([], [])

    for i in range(1, n // 2 + 1):
        for a in combinations(lst, i):
            a = list(a)
            b = lst[:]
            for x in a:
                b.remove(x)
            diff = abs(sum(a) - sum(b))
            if diff < best_diff:
                best_diff = diff
                best_pair = (a, b)
                if best_diff == 0:
                    return best_pair

    return best_pair

lst = [7, 3, 2, 5, 8, 1]
left, right = split_min_diff(lst)
print("Original list:", lst)
print("Sublist 1:", left, "Sum:", sum(left))
print("Sublist 2:", right, "Sum:", sum(right))
print("Sum difference:", abs(sum(left) - sum(right)))