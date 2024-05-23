#Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are common keys, the values should be added together IN PYTHON


def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key exists in the merged dictionary, add the values
            merged_dict[key] += value
        else:
            # If the key doesn't exist in the merged dictionary, add it with its value
            merged_dict[key] = value
    return merged_dict

# Example usage:
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged_dict = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", merged_dict)

