#Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list in python


def word_frequency(words):
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

word_list = input("Enter a list of words separated by spaces: ").split()
word_freq = word_frequency(word_list)
print("Word frequencies:", word_freq)
