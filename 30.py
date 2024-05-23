#Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of these two sets
# Prompting the user to input the first set of strings
set1_input = input("Enter the first set of strings (separated by spaces): ")

# Splitting the input string into individual strings and creating a set
set1 = set(set1_input.split())

# Prompting the user to input the second set of strings
set2_input = input("Enter the second set of strings (separated by spaces): ")

# Splitting the input string into individual strings and creating a set
set2 = set(set2_input.split())

# Calculating the symmetric difference of the two sets
symmetric_difference = set1.symmetric_difference(set2)

# Printing the symmetric difference
print("Symmetric Difference of the two sets:", symmetric_difference)
