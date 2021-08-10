# function that takes a list and returns a string with all items in the list
def lst_to_string(lst):
# each list element should be separated with a comma and space.  The last element should be preceded by ', and'
    last_element = lst.pop()
    joined_string = ", ".join(lst)
    return "last element:", last_element, "joined string:", joined_string
# should work with any list, including empty lists
# example: 
# spam = ['apples', 'bananas', 'tofu', 'cats'] should yield 'apples, bananas, tofu, and cats'

test_lst = ['apples', 'bananas', 'tofu', 'cats']

print(lst_to_string(test_lst))