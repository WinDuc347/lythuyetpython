### FUNCTION DEFINITIONS ###

def supermarket(weekday, bought_alcohol):
    # YOUR CODE HERE
    
    expenses = 0
    if weekday == "Monday":
        expenses = 40
    else:
        expenses = 10
        
    if bought_alcohol:
        expenses *= 2
    return expenses

def buy_textbooks(willingness_to_pay, accokaart):
    # YOUR CODE HERE
    
    if willingness_to_pay == 0:
        return 0;
    elif willingness_to_pay == 1:
        return 200
    elif willingness_to_pay == 2:
        if accokaart:
            return 400*0.9 + 30
        else:
            return 400
    elif willingness_to_pay == 3:
        if accokaart:
            return 700*0.9 + 30
        else:
            return 700

def calc_fine(alcohol_level):
    # YOUR CODE HERE
    
    if alcohol_level < 0.005:
        return 0
    elif alcohol_level >= 0.005 and alcohol_level <= 0.008:
        return 50
    elif alcohol_level > 0.008 and alcohol_level <= 0.015:
        return (1/7)*(100000*alcohol_level - 450)
    elif alcohol_level > 0.015:
        return 250

### MAIN PROGRAM ###
total_cost = 0
super_cost = supermarket('Monday', True)
book_cost = buy_textbooks(3, False)
fine_cost = calc_fine(0.68)
total_cost = super_cost + book_cost + fine_cost

### TEST CODE ###
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
final_grade = 0

print("TEST 1: SUPERMARKET... (max 4 points)")

super1 = supermarket('Monday', False)
if super1 == 40:
    final_grade = final_grade + 1

super2 = supermarket('Monday', True)
if super2 == 80:
    final_grade = final_grade + 1

super3 = supermarket('Tuesday', False)
if super3 == 10:
    final_grade = final_grade + 1

super4 = supermarket('Friday', True)
if super4 == 20:
    final_grade = final_grade + 1

print("TEST 2: TEXTBOOKS... (max 6 points)")
books1 = buy_textbooks(0, False)
books2 = buy_textbooks(0, True)
if books1 == books2 == 0:
    final_grade = final_grade + 1
    
books3 = buy_textbooks(1, False)
books4 = buy_textbooks(1, True)
if books3 == books4 == 200:
    final_grade = final_grade + 1

books5 = buy_textbooks(2, False)
if books5 == 400:
    final_grade = final_grade + 1
    
books6 = buy_textbooks(3, False)
if books6 == 700:
    final_grade = final_grade + 1

books7 = buy_textbooks(2, True)
if books7 == 390:
    final_grade = final_grade + 1
    
books8 = buy_textbooks(3, True)
if books8 == 660:
    final_grade = final_grade + 1

print("TEST 3: FINES... (max 6 points)")

fine1 = calc_fine(0.004)
if fine1 == 0:
    final_grade = final_grade + 1
  
fine2 = calc_fine(0.005)
if fine2 == 50:
    final_grade = final_grade + 1

fine3 = calc_fine(0.008)
if fine3 == 50:
    final_grade = final_grade + 1
    
fine4 = calc_fine(0.015)
if fine4 == 150:
    final_grade = final_grade + 1
    
fine5 = calc_fine(0.0115)
if fine5 == 100:
    final_grade = final_grade + 1

fine6 = calc_fine(0.99)
if fine6 == 250:
    final_grade = final_grade + 1

print("TEST 4: TOTAL COST... (max 1 point)")
if total_cost == 1030:
    final_grade = final_grade + 1

print("Your score for this exercise is ", final_grade, "/17.")
    
