# Given tuple
#num_tuple = tuple(input("Enter a sequence of your list: ").split(","))
#print("Given tuple is ", num_tuple)
num_tuple = (10, 20, 33, 46, 55)
print("Given list is ", num_tuple)

# Print elements that are divisible by 5
print("Elements that are divisible by 5:")
for num in num_tuple:
    if (num % 5 == 0):
        print(num)