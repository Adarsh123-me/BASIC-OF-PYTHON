#4.Write a code to check if two given strings are anagrams of each other
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    return sorted_str1 == sorted_str2

input_str1 = "listen"
input_str2 = "silent"
if are_anagrams(input_str1, input_str2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")
