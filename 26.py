#Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets

# Prompting the user to input the first set of characters
set1_input = input("Enter the first set of characters (separated by spaces): ")

# Splitting the input string into individual characters and creating a set
set1 = set(set1_input.split())

# Prompting the user to input the second set of characters
set2_input = input("Enter the second set of characters (separated by spaces): ")

# Splitting the input string into individual characters and creating a set
set2 = set(set2_input.split())

# Calculating the union of the two sets
union_set = set1.union(set2)

# Printing the union set
print("Union of the two sets:", union_set)
