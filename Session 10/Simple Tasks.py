# TASK 1 [1 point] #
def count_runners( km_list ):

    return len(km_list)

# TASK 2 [1 point] #
def check_km_value( km_value ):
    
    if km_value<5:
        return "not ready"
    elif km_value>10:
        return "good"
    else:
        return "intermediate"
    
# TASK 3 [2 points] #
def average_km( km_list ):
    
    total = 0
    
    for i in km_list:
        total+=i
    
    if len(km_list) > 0:
        return total/len(km_list)
    return 0

# TASK 4 [2 points] #
def find_km( km_list, km_value ):
    
    total = 0
    
    for i in km_list:
        if i == km_value:
            total += 1
    return total

# TASK 5 [2 points] #
def km_values_above( km_list ):
    
    total_amount = []
    
    for i in km_list:
        total_amount.append(round(i/7, 1))
    
    new_list = []
    
    for i in total_amount:
        if i>1:
            new_list.append(i)
    
    return new_list

# TASK 6 [3 points] #
def km_age_above( km_list, age_list ):
    
    new_list = km_list.copy()

    for i in range(len(age_list)):
        if age_list[i] >= 50:
            new_list[i]+=5            
                
    return new_list

# TASK 7 [3 points] #
def age_good( runner_matrix ):
    
    total_age = 0
    total_amount = 0
    
    for i in runner_matrix:
        if check_km_value(i[0]) == "good":
            total_age+=i[1]
            total_amount+=1
    
    if total_amount != 0:
        return total_age/total_amount
    return 0

### DO NOT TOUCH THE CODE BELOW THIS LINE ###

def evaluation():
    
    runners = [10, 3, 11, 22, 4, 8, 5, 5, 8, 19, 11, 14, 2, 0, 12, 0, 4, 11, 20, 6]
    age = [16, 31, 41, 22, 45, 28, 56, 15, 38, 19, 61, 19, 20, 30, 22, 40, 45, 18, 20, 16]
    runners_age = [[10,16],[3,31],[11,41],[22,22],[4,45],[8,28],[5,56],[5,15],[8,38],[19,19],[11,61],[14,19],[2,20],[0,30],[12,22],[0,40],[4,45],[11,18],[20,20],[6,16]] 

    result = 0
    
    # TEST TASK 1 #
    t1_1 = count_runners(runners)
    t1_2 = count_runners([])
    if t1_1 == 20 and t1_2 == 0:
        result += 1
        print("# TEST 1 SUCCESSFUL #")
    else: print("# TEST 1 FAILED #")
    
    # TEST TASK 2 #
    t2_1 = check_km_value(2)
    t2_2 = check_km_value(13)
    t2_3 = check_km_value(10)
    
    if t2_1 == "not ready" and t2_2 == "good" and t2_3 == "intermediate":
        result += 1
        print("# TEST 2 SUCCESSFUL #")
    else: print("# TEST 2 FAILED #")
    
    # TEST TASK 3 #
    t3_1 = average_km(runners)
    t3_2 = average_km([])
    
    if t3_1 == 8.75 and t3_2 == 0:
        result += 2
        print("# TEST 3 SUCCESSFUL #")
    else: print("# TEST 3 FAILED #")
    
    # TEST TASK 4 #
    t4_1 = find_km(runners, 8)
    t4_2 = find_km([], 4)
    t4_3 = find_km(runners, 1)
    
    if t4_1 == 2 and t4_2 == 0 and t4_3 == 0:
        result += 3
        print("# TEST 4 SUCCESSFUL #")
    else: print("# TEST 4 FAILED #")
    
    # TEST TASK 5 #
    t5_1 = km_values_above(runners)
    t5_2 = km_values_above([])
    
    if t5_1 == [1.4, 1.6, 3.1, 1.1, 1.1, 2.7, 1.6, 2.0, 1.7, 1.6, 2.9] and t5_2 == []:
        result+=2
        print("# TEST 5 SUCCESSFUL #")
    else: print("# TEST 5 FAILED #")
    
    # TEST TASK 6 #
    t6_1 = km_age_above(runners, age)
    t6_2 = km_age_above(runners, [])
    
    if t6_1 == [10, 3, 11, 22, 4, 8, 10, 5, 8, 19, 16, 14, 2, 0, 12, 0, 4, 11, 20, 6] and t6_2 == [10, 3, 11, 22, 4, 8, 5, 5, 8, 19, 11, 14, 2, 0, 12, 0, 4, 11, 20, 6]:
        result+=3
        print("# TEST 6 SUCCESSFUL #")
    else: print("# TEST 6 FAILED #")
    
    # TEST TASK 7 #
    t7_1 = age_good(runners_age)
    t7_2 = age_good([])
    
    if t7_1 == 27.75 and t7_2 == 0:
        result+=3
        print("# TEST 7 SUCCESSFUL #")
    else: print("# TEST 7 FAILED #")
    
    print()    
    print("Tentative overall score: ", result, "/ 15")
    print()
    print("This is an indicative value only. You also need to follow the instructions of the exam,")
    print("and code in a flexible way (i.e., your code still needs to work when tested with different values).")
    

if __name__ == "__main__":
    evaluation()