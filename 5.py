#5. Write a code to find all occurrences of a given substring within another string

def find_all_occurrences(main_string, sub_string):
    occurrences = []
    start_index = 0
    
    while True:
        index = main_string.find(sub_string, start_index)
        if index == -1:
            break
        occurrences.append(index)
        start_index = index + 1
    
    return occurrences

main_string = "hellohellohellohello"
sub_string = "hello"
result = find_all_occurrences(main_string)
