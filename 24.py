#Develop a code that prompts the user to input two sets of strings. Then, print the elements that are present in the first set but not in the second set
def get_elements_not_in_second_set():
    # Prompt the user to enter two sets of strings separated by commas
    input_set1 = input("Enter the first set of strings separated by commas: ")
    input_set2 = input("Enter the second set of strings separated by commas: ")
    
    # Convert input strings to sets of strings
    set1 = set(input_set1.split(','))
    set2 = set(input_set2.split(','))
    
    # Find elements that are present in the first set but not in the second set
    elements_not_in_second_set = set1 - set2
    
    return elements_not_in_second_set

# Get the elements and print the result
elements_not_in_second_set = get_elements_not_in_second_set()
print("Elements present in the first set but not in the second set:", elements_not_in_second_set)
