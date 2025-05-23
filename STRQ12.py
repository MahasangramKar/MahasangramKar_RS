
data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)
averages = [sum(col) / len(col) for col in zip(*data)]
print("Average column-wise:", averages)
