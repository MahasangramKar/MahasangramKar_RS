n= int(input("Enter the value of n : "))
def print_sum_of_squares(n):
    for i in range(1, n + 1):
        total = sum(j**2 for j in range(1, i + 1))
        print(f"Sum of squares from 1 to {i} is: {total}")
print_sum_of_squares(n)
