#Create a code that take sat up leand two integers as input.The function should return a new tuple containing elements from the original tuple within the specified range of indice in python

def get_elements_within_range(input_tuple, start_index, end_index):
    new_tuple = input_tuple[start_index:end_index+1]
    return new_tuple

input_tuple = (1, 2, 3, 4, 5, 6, 7)
start_index = 2
end_index = 5
result_tuple = get_elements_within_range(input_tuple, start_index, end_index)
print("Original tuple:", input_tuple)
print("New tuple containing elements within the specified range:", result_tuple)
