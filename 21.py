#Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples

def find_common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Find the intersection of the sets
    common_elements = set1.intersection(set2)
    
    # Convert the intersection set back to a tuple
    common_tuple = tuple(common_elements)
    
    return common_tuple

# Test the function
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common_elements = find_common_elements(tuple1, tuple2)
print("Common elements in tuple1 and tuple2:", common_elements)
