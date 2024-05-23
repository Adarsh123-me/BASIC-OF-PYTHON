#8.Write a code to convert a given string to uppercase or lowercase
def convert_to_uppercase(input_str):
    return input_str.upper()

def convert_to_lowercase(input_str):
    return input_str.lower()

input_str = "Hello, World!"
uppercase_str = convert_to_uppercase(input_str)
lowercase_str = convert_to_lowercase(input_str)

print("Original String:", input_str)
print("Uppercase String:", uppercase_str)
print("Lowercase String:", lowercase_str)
