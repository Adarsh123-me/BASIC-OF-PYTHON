#2.  Write a code to count the number of vowels in a string
def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count

input_str = "Hello, World!"
num_vowels = count_vowels(input_str)
print("Number of vowels in the string:", num_vowels)
