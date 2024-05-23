#7.Write a code to determine if a string has all unique characters
def has_unique_characters(input_str):
    # Create a set to store unique characters encountered
    unique_chars = set()
    
    # Iterate through each character in the string
    for char in input_str:
        # If the character is already in the set, it means it's not unique
        if char in unique_chars:
            return False
        # Otherwise, add it to the set
        else:
            unique_chars.add(char)
    
    # If loop completes without returning False, all characters are unique
    return True

# Test the function
input_str = "abcdefg"
if has_unique_characters(input_str):
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")
