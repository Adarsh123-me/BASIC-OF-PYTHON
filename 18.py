#Implement a code to find the intersection of two given lists
def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection of the sets
    intersection = set1.intersection(set2)
    
    # Convert the intersection back to a list
    intersection_list = list(intersection)
    
    return intersection_list

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print("Intersection of list1 and list2:", intersection)
