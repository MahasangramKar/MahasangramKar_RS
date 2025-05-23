
user_input = input("Enter elements separated by space: ")
user_list = user_input.split()
def all_unique(lst):
    return len(lst) == len(set(lst))

if all_unique(user_list):
    print("All elements are unique.")
else:
    print("There are duplicate elements.")
