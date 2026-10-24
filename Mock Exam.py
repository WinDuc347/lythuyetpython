                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 # TASK 1 [1 point] #
def bottles_in_bag(bag):
    number = len(bag)
    return number

# TASK 2 [1 point] #
def check_deposit_value(deposit_value):
    if deposit_value >= 25:
        return True
    return False

# TASK 3 [2 points] #
def bottle_count_in_bag(targetbrand, bag_brands):
    number = 0
    for i in bag_brands:
        if i == targetbrand:
            number+=1            
    return number

# TASK 4 [3 points] #
def apply_bonus(deposit_values):
    new_values = deposit_values.copy()
    for i in new_values:
        new_values[new_values.index(i)]*=1.2
    return new_values

# TASK 5 [3 points] #
def calculate_bonus(bag_brands, deposit_values):
    new_values = deposit_values.copy()
    number = 0
    i = 0
    number = 0
    while i < len(bag_brands):
        new_values = deposit_values.copy()        
        if bag_brands[i] == "Stella":
            number+=1
            if number >= 5:
                j = 0
                while j < len(bag_brands):
                    if bag_brands[j] == "Stella":
                        new_values[j] = 100
                    j+=1
                break
        i+=1       
    return new_values

### DO NOT TOUCH THE CODE BELOW THIS LINE ###

def evaluation():
    result = 0
    
    # TEST TASK 1 #
    t1_1 = bottles_in_bag(['Stella', 'Spa', 'Coca-Cola', 'Coca-Cola', 'Pepsi', 'Spa', 'Spa', 'Spa'])
    t1_2 = bottles_in_bag([])
    t1_3 = bottles_in_bag(['Stella', 'Spa'])
    if t1_1 == 8 and t1_2 == 0 and t1_3 == 2:
        result += 1
        print("# TEST 1 SUCCESSFUL #")
    else: print("# TEST 1 FAILED #")
    
    # TEST TASK 2 #
    t2_1 = check_deposit_value(20)
    t2_2 = check_deposit_value(25)
    t2_3 = check_deposit_value(-25)
    
    if t2_1 == False and t2_2 == True and t2_3 == False:
        result += 1
        print("# TEST 2 SUCCESSFUL #")
    else: print("# TEST 2 FAILED #")
    
    # TEST TASK 3 #
    t3_1 = bottle_count_in_bag('Spa', ['Spa', 'Coca-Cola', 'Spa', 'Spa', 'Coca-Cola', 'Spa'])
    t3_2 = bottle_count_in_bag('Pepsi', ['Coca-Cola', 'Coca-Cola', 'Coca-Cola', 'Pepsi', 'Spa', 'Spa', 'Spa', 'Spa'])
    t3_3 = bottle_count_in_bag('Coca-Cola', [])
    
    if t3_1 == 4 and t3_2 == 1 and t3_3 == 0:
        result += 2
        print("# TEST 3 SUCCESSFUL #")
    else: print("# TEST 3 FAILED #")
    
    # TEST TASK 4 #
    t4_1 = apply_bonus([50,10,50])
    t4_2 = apply_bonus([])
    t4_3 = apply_bonus([100, 600, 300])
    
    if t4_1 == [60, 12, 60] and t4_2 == [] and t4_3 == [120, 720, 360]:
        result += 3
        print("# TEST 4 SUCCESSFUL #")
    else: print("# TEST 4 FAILED #")
    
    # TEST TASK 5 #
    t5_1 = calculate_bonus(['Spa', 'Stella', 'Pepsi'], [10,25,50])
    t5_2 = calculate_bonus([],[])
    t5_3 = calculate_bonus(['Spa', 'Stella', 'Stella','Spa', 'Stella', 'Stella','Stella', 'Pepsi'],[10,25,25,10,25,25,25,50])
    
    if t5_1 == [10,25,50] and t5_2 == [] and t5_3 == [10,100,100,10,100,100,100,50]:
        result+=3
        print("# TEST 5 SUCCESSFUL #")
    else: print("# TEST 5 FAILED #")
    
    print()    
    print("Tentative overall score: ", result, "/ 10")
    print()
    print("This is an indicative value only. You also need to follow the instructions of the exam,")
    print("and code in a flexible way (i.e., your code still needs to work when tested with different values).")
    

if __name__ == "__main__":
    evaluation()
    
