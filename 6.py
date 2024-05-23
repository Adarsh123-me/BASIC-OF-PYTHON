#6.Write a code to perform basic string compression using the counts of repeated character
def compress_string(input_str):
    compressed_str = ""
    count = 1
    # Loop through the string starting from the second character
    for i in range(1, len(input_str)):
        # If current character is same as previous character, increment count
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            # If current character is different from previous character,
            # append previous character and its count to the compressed string
            compressed_str += input_str[i - 1] + str(count)
            # Reset count for the new character
            count = 1
    
    # Append the last character and its count
    compressed_str += input_str[-1] + str(count)
    
    # If compressed string is longer than original string, return original string
    if len(compressed_str) >= len(input_str):
        return input_str
    else:
        return compressed_str

# Test the function
input_str = "aabcccccaaa"
compressed = compress_string(input_str)
print("Original String:", input_str)
print("Compressed String:", compressed)
