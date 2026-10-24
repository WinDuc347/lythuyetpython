#Exercise 3
def get_shortest_list(list_1, list_2):
    """Return the shortest list, or the first list if both are equally long.
    
    Parameters:
    list_1 (list) -- The first list of elements.
    list_2 (list) -- The second list of elements.
    """
    if len(list_1) > len(list_2):
        return list_2
    else:
        return list_1

#Exercise 4
def count(element_list, element):
    """Return the number of occurrences of element in the list.
    
    Parameters:
    element_list (list) -- The list of elements.
    element (any type) -- The element that is counted.
    """
    counter = 0
    for i in element_list:
        if i == element:
            counter += 1
    return counter

#Exercise 5
def contains_element(element_list, element):
    """Return True if element is in the list.
    
    Parameters:
    element_list (list) -- The list of elements.
    element (any type) -- The element to look for in the list.
    """
    for i in element_list:
        if i == element:
            return True
    return False

#Exercise 6
def last_occurrence(element_list, element):
    """Return the index of the last occurrence of element in the list.
    
    Parameters:
    element_list (list) -- The list of elements.
    element (any type) -- The element of which the last occurrence's index is returned.
    """
    i = len(element_list) - 1
    
    while i >= 0:
        if element_list[i] == element:
            return i
        i -= 1
        
    return -1

#Exercise 7a
def divisors(number):
    """Return a list of all divisors of number in ascending order.

    Parameters:
    number (int) -- The number of which the function computes all divisors.
    """
    divisors = []
    
    i = 1
    
    while i <= number:
        if number % i == 0:
            divisors += [i]
        i += 1
    
    return divisors

#Exercise 7b
def divisors_high_to_low(number):
    """Return a list of all divisors of number in ascending order.

    Parameters:
    number (int) -- The number of which the function computes all divisors.
    """
    divisors = []
    
    i = number
    
    while i > 0:
        if number % i == 0:
            divisors += [i]
        i -= 1
    
    return divisors

#Exercise 8
def find_largest_number(number_list):
    """Return the largest number in the list.
    
    Parameters:
    number_list (list) -- The list of numbers.
    """
    number = number_list[0]
    
    for i in number_list:
        if i > number:
            number = i
            
    return number

#Exercise 9
def replace(element_list, element_to_replace, new_element):
    """Replace an element in the list and return the updated list.
    
    Parameters:
    element_list (list) -- The list of elements.
    element_to_replace (any type) -- The element of which its second occurrence needs to be replaced.
    new_element (any type) -- The new element that will be in element_to_replace's place.
    """
    counter = 0
    counter2 = 0
    new_list = element_list.copy()
    
    for i in element_list:
        if i == element_to_replace:
            counter += 1
            if counter == 2:
                new_list[counter2] = new_element
                return new_list
        counter2 += 1
            
    return new_list

#Exercise 10
def count_x_y(count_string):
    """Return the number of times there's one character between x and y.

    Parameters:
    count_string (string) -- The string the function uses to count how many times the condition is fulfilled.
    """
    i = 0
    counter = 0
    
    while i < len(count_string) - 2:
        if count_string[i] == "x":
            if  count_string[i+2] == "y":
                counter += 1
        elif count_string[i] == "y":
            if  count_string[i+2] == "x":
                counter += 1
        i += 1
        
    return counter
    
#Exercise 11
def is_palindrome(string_to_check):
    """Return True if the given string is a palindrome.

    Parameters:
    string_to_check (int) -- The string to check if it is palindromic.
    """
    
    copy = ""
    i = len(string_to_check) - 1
    
    while i >= 0:
        copy += string_to_check[i]
        i -= 1
        
    if copy == string_to_check:
        return True
    return False


#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
score = 0

if get_shortest_list([0], [0]) != "Not implemented yet":
    print("Testing exercise 3...")
    success = True
    if get_shortest_list([1, -8, 6], [9, 7]) != [9, 7]:
        success = False
        print("--- Test 3-A failed")
    if get_shortest_list([9, 9, 9], [4, 0, 1]) != [9, 9, 9]:
        success = False
        print("--- Test 3-B failed")
    if get_shortest_list([1], [0, 3]) != [1]:
        success = False
        print("--- Test 3-C failed")
    if get_shortest_list("string", "much longer string") != "string":
        success = False
        print("--- Test 3-D failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if count([], " ") != "Not implemented yet":
    print("Testing exercise 4...")
    success = True
    if count(["a","b","c"], "a") != 1:
        success = False
        print("--- Test 4-A failed")
    if count([7, 8, 4, 2, 2, 2], 2) != 3:
        success = False
        print("--- Test 4-B failed")
    if count("test string", "T") != 0:
        success = False
        print("--- Test 4-C failed")
    if count([], 0) != 0:
        success = False
        print("--- Test 4-D failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if contains_element([], " ") != "Not implemented yet":
    print("Testing exercise 5...")
    success = True
    if not contains_element(["a","b","c"], "a"):
        success = False
        print("--- Test 5-A failed")
    if not contains_element([7, 8, 4, 2, 2, 0], 0):
        success = False
        print("--- Test 5-B failed")
    if not contains_element("test string", "r"):
        success = False
        print("--- Test 5-C failed")
    if contains_element("test string", "T"):
        success = False
        print("--- Test 5-D failed")
    if contains_element([], "x"):
        success = False
        print("--- Test 5-E failed")
    if contains_element([7, 8, 4, 2, 2, 0], 3):
        success = False
        print("--- Test 5-F failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if last_occurrence([], " ") != "Not implemented yet":
    print("Testing exercise 6...")
    success = True
    if last_occurrence([5, 3, 8], 3) != 1:
        success = False
        print("--- Test 6-A failed")
    if last_occurrence([7, 8, 4, 2, 2, 2], 2) != 5:
        success = False
        print("--- Test 6-B failed")
    if last_occurrence("yxx", "y") != 0:
        success = False
        print("--- Test 6-C failed")
    if last_occurrence([], 0) != -1:
        success = False
        print("--- Test 6-D failed")
    if last_occurrence(["a", "b", "c"], "x") != -1:
        success = False
        print("--- Test 6-E failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if divisors(1) != "Not implemented yet":
    print("Testing exercise 7a...")
    success = True
    if divisors(6) != [1, 2, 3, 6]:
        success = False
        print("--- Test 7a-A failed")
    if divisors(1) != [1]:
        success = False
        print("--- Test 7a-B failed")
    if divisors(97) != [1, 97]:
        success = False
        print("--- Test 7a-C failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")
        
if divisors_high_to_low(1) != "Not implemented yet":
    print("Testing exercise 7b...")
    success = True
    if divisors_high_to_low(6) != [6, 3, 2, 1]:
        success = False
        print("--- Test 7b-A failed")
    if divisors_high_to_low(1) != [1]:
        success = False
        print("--- Test 7b-B failed")
    if divisors_high_to_low(97) != [97, 1]:
        success = False
        print("--- Test 7b-C failed")
    if divisors_high_to_low(20) != [20, 10, 5, 4, 2, 1]:
        success = False
        print("--- Test 7b-C failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if find_largest_number([1]) != "Not implemented yet":
    print("Testing exercise 8...")
    success = True
    if find_largest_number([4, 3, 9, 0, -1, 7]) != 9:
        success = False
        print("--- Test 8-A failed")
    if find_largest_number([14, 3, 9, 0, -1, 7]) != 14:
        success = False
        print("--- Test 8-B failed")
    if find_largest_number([3, 3, -3, 3, 3]) != 3:
        success = False
        print("--- Test 8-C failed")
    if find_largest_number([0.3, -1.4, 0.3, -4.5]) != 0.3:
        success = False
        print("--- Test 8-D failed")
    if find_largest_number([-9876000, -9000111, -9876000]) != -9000111:
        success = False
        print("--- Test 8-E failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if replace([], " ", " ") != "Not implemented yet":
    print("Testing exercise 9...")
    success = True
    if replace(["a", "h", "b", "f", "a", "a", "z"], "a", "-") != ["a", "h", "b", "f", "-", "a", "z"]:
        success = False
        print("--- Test 9-A failed")
    if replace(["+", "+", "+", "+", "+", "+"], "+", "9") != ["+", "9", "+", "+", "+", "+"]:
        success = False
        print("--- Test 9-B failed")
    if replace([0, 4, 2, 2, 3], 0, 7) != [0, 4, 2, 2, 3]:
        success = False
        print("--- Test 9-C failed")
    if replace([0, 4, 2, 2, 3], 4, 7) != [0, 4, 2, 2, 3]:
        success = False
        print("--- Test 9-D failed")
    if replace([0, 4, 3, 2, 2], 2, 4) != [0, 4, 3, 2, 4]:
        success = False
        print("--- Test 9-E failed")
    if replace([], "x", " ") != []:
        success = False
        print("--- Test 9-F failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if count_x_y(" ") != "Not implemented yet":
    print("Testing exercise 10...")
    success = True
    if count_x_y("xzy") != 1:
        success = False
        print("--- Test 10-A failed")
    if count_x_y("axyyx8yx") != 3:
        success = False
        print("--- Test 10-B failed")
    if count_x_y("axyiylxy") != 1:
        success = False
        print("--- Test 10-C failed")
    if count_x_y("xy") != 0:
        success = False
        print("--- Test 10-D failed")
    if count_x_y("x") != 0:
        success = False
        print("--- Test 10-E failed")
    if count_x_y("xxxxyyyy") != 2:
        success = False
        print("--- Test 10-F failed")
    if count_x_y("yzx") != 1:
        success = False
        print("--- Test 10-G failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")

if is_palindrome("A") != "Not implemented yet":
    print("Testing exercise 11...")
    success = True
    if not is_palindrome("rotor"):
        success = False
        print("--- Test 11-A failed")
    if not is_palindrome("X"):
        success = False
        print("--- Test 11-B failed")
    if not is_palindrome("qRRq"):
        success = False
        print("--- Test 11-C failed")
    if not is_palindrome("6gTXq+;f4f;+qXTg6"):
        success = False
        print("--- Test 11-D failed")
    if is_palindrome("word"):
        success = False
        print("--- Test 11-E failed")
    if is_palindrome("dolop"):
        success = False
        print("--- Test 11-F failed")
    if success:
        print(">>> Success - 1/1")
        score = score + 1
    else:
        print(">>> Fail - 0/1")
        
print("Score: " + str(score) + "/10")
