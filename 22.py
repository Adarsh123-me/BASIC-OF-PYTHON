# Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the intersection of these two sets

def get_intersection():
    # Prompt the user to enter two sets of integers separated by commas
    input_set1 = input("Enter the first set of integers separated by commas: ")
    input_set2 = input("Enter the second set of integers separated by commas: ")
    
    # Convert input strings to sets of integers
    set1 = set(map(int, input_set1.split(',')))
    set2 = set(map(int, input_set2.split(',')))
    
    # Find the intersection of the sets
    intersection = set1.intersection(set2)
    
    return intersection

# Get the intersection and print the result
intersection = get_intersection()
print("Intersection of the two sets:", intersection)
