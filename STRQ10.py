
arr1_input = input("Enter elements of first array separated by space: ")
arr1 = arr1_input.split()
arr2_input = input("Enter elements of second array separated by space: ")
arr2 = arr2_input.split()

missing = set(arr1) - set(arr2)
print("Missing elements from second array:", missing)
