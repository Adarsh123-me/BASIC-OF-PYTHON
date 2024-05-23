#mplement a code to find and remove duplicates from a list while preserving the original order of elements  in python
def remove_duplicates_preserve_order(lst):
    # Initialize an empty dictionary to store unique elements
    seen = {}
    result = []

    # Iterate through the list
    for element in lst:
        # If the element is not in the dictionary, add it to the dictionary and result list
        if element not in seen:
            seen[element] = True
            result.append(element)

    return result

# Test the function
my_list = [1, 2, 3, 2, 4, 3, 5]
unique_elements = remove_duplicates_preserve_order(my_list)
print("Original list:", my_list)
print("List after removing duplicates:", unique_elements)
