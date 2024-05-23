#
#Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys and their counts as value in python
def count_occurrences(lst):
    # Initialize an empty dictionary to store element counts
    element_counts = {}
    
    # Iterate through the list
    for element in lst:
        # If the element is already in the dictionary, increment its count
        if element in element_counts:
            element_counts[element] += 1
        # If the element is not in the dictionary, add it with count 1
        else:
            element_counts[element] = 1
    
    return element_counts

# Test the function
my_list = [1, 2, 3, 2, 1, 4, 2, 5]
occurrences = count_occurrences(my_list)
print("Occurrences of each element:", occurrences)
