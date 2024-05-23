#Implement a code to find the second largest number in a given list of integers
def find_second_largest(numbers):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Check if the list has at least two elements
    if len(sorted_numbers) < 2:
        return "List should have at least two elements"
    
    # Return the second largest number
    return sorted_numbers[-2]

# Test the function
numbers = [10, 5, 20, 15, 25]
second_largest = find_second_largest(numbers)
print("Second largest number:", second_largest)
