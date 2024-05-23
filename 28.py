#Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these two sets in python

# Define two sets of integers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print the sets
print("Set 1:", set1)
print("Set 2:", set2)

# Calculate and print the union of the two sets
union = set1.union(set2)
print("Union of Set 1 and Set 2:", union)

# Calculate and print the intersection of the two sets
intersection = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection)

# Calculate and print the difference between the two sets (elements in set1 but not in set2)
difference_set1_set2 = set1.difference(set2)
print("Difference between Set 1 and Set 2:", difference_set1_set2)

# Calculate and print the difference between the two sets (elements in set2 but not in set1)
difference_set2_set1 = set2.difference(set1)
print("Difference between Set 2 and Set 1:", difference_set2_set1)
