# Develop a code that takes a tuple of integers as input. The function should return the maximum and minimum values from the tuple using tuple unpacking

def find_min_max(input_tuple):
    min_value = min(input_tuple)
    max_value = max(input_tuple)
    return min_value, max_value

input_tuple = (3, 8, 1, 6, 4, 9, 2)
min_val, max_val = find_min_max(input_tuple)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
