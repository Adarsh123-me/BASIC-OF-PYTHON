#&Writeacodethatinvertsadictionary,swappingkeysandvalues.Ensurethattheinverteddictionary correctly handles cases where multiple keys have the same value by storing the keys as a list in the inverted dictionary
def invert_dict(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict

input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
inverted_dict = invert_dict(input_dict)
print("Original Dictionary:", input_dict)
print("Inverted Dictionary:", inverted_dict)
