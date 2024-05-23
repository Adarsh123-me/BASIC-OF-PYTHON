#3. Write a code to check if a given string is a palindrome or not 
def is_palindrome(input_str):
    
    input_str = input_str.lower()
    input_str = input_str.replace(" ", "")
    return input_str == input_str[::-1]

input_str = "A man a plan a canal Panama"
result = is_palindrome(input_str)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
