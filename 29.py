#Write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given element in the tuple
def count_occurrences(input_tuple, element):
    count = input_tuple.count(element)
    return count

my_tuple = (1, 2, 3, 4, 2, 5, 2, 6)
element_to_count = 2
occurrences = count_occurrences(my_tuple, element_to_count)
print("Number of occurrences of", element_to_count, "in the tuple:", occurrences)
