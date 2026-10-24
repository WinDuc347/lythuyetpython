+#a
def positive_numbers(num_list):
    new_list = []
    for i in num_list:
        if i >= 0:
            new_list.append(i)
    return new_list

#b
def sort(num_list):
    # Make new list with only positive numbers 
    positive_list = positive_numbers(num_list)
    
    # Sort positive list
    new_list = sorted(positive_list)
    
    return new_list

#c
def square(num_list):
    new_list = []
    for i in num_list:
        new_list.append(i*i)
    
    return new_list

#d
def large_square(num_list):
    new_list = []
    for i in num_list:
        if i*i >= 1000:
            new_list.append(i)
    return new_list

#e
def fibonacci():
    num_list = [1,1]
    i = 2
    while True:
        number = num_list[i-2]+num_list[i-1]
        if number <= 100:
            num_list.append(number)
        else:
            break
        i+=1
    return num_list

#f
def find_fib(num_list):
    new_list = []
    fib_list = fibonacci()
    
    for i in num_list:
        if i in fib_list:
            new_list.append(i)
    
    return new_list

#g
def lottery(num_list):
    sorted_list = sort(num_list)
    if len(sorted_list) == 6:
        print("The winning numbers are", sorted_list)
    else:
        print(len(sorted_list), " is not the correct amount of numbers to play")

#Tests
print(sort([1,2,3,4,-5,-7,0]))
print(square([1,2,3,4,-5,-7,0]))
print(large_square([100,25,38,49,-5,-7,0]))
print(fibonacci())
print(find_fib([1,2,3,4,-5,-7,0]))

