# Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You can choose whether to sort in ascending or descending order

def sort_dict_by_values(input_dict, reverse=False):
    # Sorting the dictionary items based on their values
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=reverse)
    # Creating a new dictionary from the sorted items
    sorted_dict = dict(sorted_items)
    return sorted_dict

# Example usage:
input_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
sorted_dict_asc = sort_dict_by_values(input_dict)
sorted_dict_desc = sort_dict_by_values(input_dict, reverse=True)

print("Sorted Dictionary (Ascending):", sorted_dict_asc)
print("Sorted Dictionary (Descending):", sorted_dict_desc)
