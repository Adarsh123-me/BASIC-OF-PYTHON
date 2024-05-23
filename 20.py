# Write a code to shuffle a given list randomly without using any built-in shuffle functions
import random

def shuffle_list(lst):
    
    # Fisher-Yates shuffle algorithm
    for i in range(len(shuffled_list) - 1, 0, -1):
        j = random.randint(0, i)  # Generate a random index between 0 and i
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]  # Swap elements at indices i and j
    
    return shuffled_list

# Test the function
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print("Original list:", my_list)
print("Shuffled list:", shuffled_list)
