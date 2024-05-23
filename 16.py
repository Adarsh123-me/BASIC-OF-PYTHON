#Create a code to check if a given list is sorted (either in ascending or descending order) or not
def is_sorted(lst):
    # Check if the list is sorted in ascending order
    if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
        return "Ascending"
    # Check if the list is sorted in descending order
    elif all(lst[i] >= lst[i+1] for i in range(len(lst)-1)):
        return "Descending"
    else:
        return "Unsorted"

# Test the function
ascending_list = [1, 2, 3, 4, 5]
descending_list = [5, 4, 3, 2, 1]
unsorted_list = [1, 3, 2, 5, 4]

print("Is ascending_list sorted?", is_sorted(ascending_list))
print("Is descending_list sorted?", is_sorted(descending_list))
print("Is unsorted_list sorted?", is_sorted(unsorted_list))
