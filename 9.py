#9. Write a code to count the number of words in a string 
def count_words(input_str):
    words = input_str.split()
    num_words = len(words)
    return num_words

input_str = "Hello, how are you?"
num_words = count_words(input_str)
print("Number of words in the string:", num_words)
