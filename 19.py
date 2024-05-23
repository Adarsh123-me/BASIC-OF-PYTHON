# Create a code to find the union of two lists without duplicates

def find_union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the union of the sets
    union_set = set1.union(set2)
    
    # Convert the union back to a list
    union_list = list(union_set)
    
    return union_list

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union = find_union(list1, list2)
print("Union of list1 and list2:", union)
