# Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the function should return None

def access_nested_dict(nested_dict, keys):
    current_dict = nested_dict
    for key in keys:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            return None
    return current_dict

nested_dict = {
    'a': {
        'b': {
            'c': 1,
            'd': 2
        },
        'e': {
            'f': 3,
            'g': 4
        }
    }
}

keys_to_access = ['a', 'b', 'd']
value = access_nested_dict(nested_dict, keys_to_access)
print("Value for keys", keys_to_access, ":", value)

keys_to_access = ['a'
