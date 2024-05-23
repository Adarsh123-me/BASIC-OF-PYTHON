#11.Write a code to remove all occurrences of a specific element from a list
def remove_element(lst, element):
    return list(filter(lambda x: x != element, lst))


my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_remove = 2
result_list = remove_element(my_list, element_to_remove)
print("Original List:", my_list)
print("List after removing {}: {}".format(element_to_remove, result_list))
