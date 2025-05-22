def find_missing(lst):
    n = len(lst) + 1
    total = n * (n + 1) // 2
    return total - sum(lst)
nums = [1, 2, 4, 5]
print("Missing number:", find_missing(nums))
