#10. Write a code to concatenate two strings without using the + operator
def concatenate_strings(str1, str2):
    return str1[:len(str1)] + str2[:len(str2)]

string1 = "Hello, "
string2 = "world!"
concatenated_string = concatenate_strings(string1, string2)
print(concatenated_string)
