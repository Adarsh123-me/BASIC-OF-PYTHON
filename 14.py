#Write a code to reverse a list in-place without using any built-in reverse functions
def reverse_list_in_place(lst):
    # Get the length of the list
    length = len(lst)
    
    # Iterate through the list up to the middle element
    for i in range(length // 2):
        # Swap elements at index i with their corresponding element from the end
        lst[i], lst[length - i - 1] = lst[length - i - 1], lst[i]

# Test the function
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
reverse_list_in_place(my_list)
print("Reversed list:", my_list)
