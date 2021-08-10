# function that takes a list and returns a string with all items in the list
def lst_to_string(lst):
# each list element should be separated with a comma and space.  The last element should be preceded by ', and'
    if type(lst) is list:
        if len(lst) > 1:
            last_element = lst.pop()
            if len(lst) == 1:
                joined_string = "" .join(lst)
                joined_string += f" and {last_element}"
                return joined_string

            else:
                joined_string = ", ".join(lst)
                joined_string += f", and {last_element}"
            
                return joined_string
        else:
            if len(lst) == 0:
                return ""
            else:
                return "".join(lst)
    else:
        return "This function requires a list."
# should work with any list, including empty lists
# example: 
# spam = ['apples', 'bananas', 'tofu', 'cats'] should yield 'apples, bananas, tofu, and cats'


test_lst_long = ['apples', 'bananas', 'tofu', 'cats']
test_lst_short = ['apples', 'cats']
test_lst_one = ['apples']
test_lst_empty = []
test_element = 1


print(lst_to_string(test_lst_long)) # tests list greater than one
print(lst_to_string(test_lst_short))
print(lst_to_string(test_lst_one))
print(lst_to_string(test_lst_empty))
print(lst_to_string(test_element))


