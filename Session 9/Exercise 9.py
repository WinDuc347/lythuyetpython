import random
import time


# Exercise 1
def show_correct_code(correct_code):
    """Print the correct code.

    Parameters:
    correct_code (string) -- The code to print.
    """
    print(correct_code)

# Exercise 2
def show_win_message(code_attempts):
    """Print a message saying the player won, with the number of tries needed.

    Parameters:
    code_attempts (list) -- The list containing all attempts.
    """   
    if len(code_attempts) > 1:
        word = "tries"
    else:
        word = "try"
    print("Well done! You've cracked the code in",len(code_attempts)," ",word,". Keep going! The game gets more challenging with a higher score.")

# Exercise 3a
def to_string(attempt):
    """Return a string representation of the given attempt.

    Parameters:
    attempt (list) -- Contains data on one (1) of the player's attempts to guess the code:
    Index 0: the code the player has entered.
    Index 1: the number of correct digits in the code.
    Index 2: the number of digits that are in the correct code, but at a wrong position.
    """
    full_string = attempt[0]+" - Correct: "+str(attempt[1])+" / Wrong position: "+str(attempt[2])
    return (full_string)

# Exercise 3b
def show_all_attempts(code_attempts):
    """Print all of the player's attempts.

    Parameters:
    code_attempts (list) -- Contains all of the player's attempts to find the code.
    """
    for i in code_attempts:
        print(to_string(i))

# Exercise 4
def has_attempts_remaining(code_attempts, max_attempts):
    """Return true if the player still has attempts remaining.

    Parameters:
    code_attempts (list) -- Contains all of the player's attempts to find the code.
    max_attempts (int) -- The maximum amount of attempts allowed.
    """
    
    return len(code_attempts) < max_attempts

# Exercise 5
def is_game_won(code_attempts):
    """Return true if the player's last attempt is correct.

    Parameters:
    code_attempts (list) -- Contains all of the player's attempts to find the code.
    """
    if len(code_attempts) == 0:
        return False
    return int(code_attempts[len(code_attempts)-1][1]) == 4

# Exercise 6a
def any_digit_exceeds_highest_digit_value(number_string_to_check, highest_digit_value):
    """Return true if any digit of the given number string is greater than the highest digit value.

    Parameters:
    number_string_to_check (string) -- The string to check, contains only numbers in string format.
    highest_digit_value (int) -- The highest value that is allowed for any digit.
    """
    for i in number_string_to_check:
        if int(i) > highest_digit_value:
            return True
    return False

# Exercise 6b
def contains_only_numbers(string_to_check):
    """Return true if the given string only contains numbers.

    Parameters:
    string_to_check (string) -- The string to check.
    """
    for i in string_to_check:
        if not i.isdigit():
            return False
    return True

# Exercise 6c
def is_valid_code_guess(code, number_of_digits, highest_digit_value):
    """Return true if code contains only numbers, has the correct length, and no digit exceeds the highest value.

    Parameters:
    code (string) -- Contains the code the player has entered.
    number_of_digits (int) -- The number of digits the code should have.
    highest_digit_value (int) -- The highest value that is allowed for any digit of the code.
    """
    if not contains_only_numbers(code):
        return False
    number = 0
    for i in code:
        if int(i) > highest_digit_value:
            return False
        number+=1

    return number == number_of_digits

# Exercise 7
def generate_code(number_of_digits, highest_digit_value):
    """Return a random string with a given length, containing unique digits, none exceeding the highest value.

    Parameters:
    number_of_digits (int) -- The number of unique digits the code should have.
    highest_digit_value (int) -- The highest value that is allowed for any digit of the code.
    """
    code = ""
    i = 0
    while i < number_of_digits:
        new_digit = str(int(random.uniform(0,highest_digit_value)))
        while new_digit in code:
            new_digit = str(int(random.uniform(0,highest_digit_value)))
        code+=new_digit
        i+=1
    return code

# Exercise 8
def get_hint(correct_code):
    """Return a string showing one digit at the correct place, and X instead of all other digits.

    Parameters:
    correct_code (string) -- The code the player has to find.
    """
    index = int(random.uniform(0,len(correct_code)))
    
    new_code = ""
    
    for i in range(len(correct_code)):
        if i == index:
            new_code+=correct_code[index]
        else:
            new_code+="X"
            
    return new_code


# Exercise 9
def compare(code, correct_code):
    """Return a list containing exactly three elements:
    Index 0 (string) -- The code the player has entered.
    Index 1 (int) -- The number of correct digits at the correct position.
    Index 2 (int) -- The number of correct digits at a wrong position.

    Parameters:
    code (string) -- The code the player has entered.
    correct_code (string) -- The code the player has to find.
    """
    correct_position = 0
    correct_digits = 0
    
    for i in range(len(code)):
        if code[i] == correct_code[i]:
            correct_position+=1
        elif code[i] in correct_code:
            correct_digits+=1
    
    final = [code, correct_position, correct_digits]
    return final


#########################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE.
#########################################

#########################################
# Test code.
#########################################

def test_code():
    """Return the number of exercises correctly implemented."""
    score = 0
    
    # Exercise 1
    # This does not test your code, but it calls the function so the result can be seen in the shell.
    show_correct_code("2431")
    
    # Exercise 2
    # This does not test your code, but it calls the function so the result can be seen in the shell.
    show_win_message([["3210", 4, 0]])
    show_win_message([["0123", 0, 4], ["3210", 4, 0]])
    
    # Exercise 3a
    if to_string(["0", 0, 0]) != "Not implemented yet":
        print("Testing exercise 3a...")
        success = True
        if to_string(["0123", 2, 1]) != "0123 - Correct: 2 / Wrong position: 1":
            success = False
            print("--- Test 3a-A failed.")
        if to_string(["2322338", 4, 0]) != "2322338 - Correct: 4 / Wrong position: 0":
            success = False
            print("--- Test 3a-B failed.")
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
    
    # Exercise 3b
    # This does not test your code, but it calls the function so the result can be seen in the shell.
    show_all_attempts([["0123", 0, 4], ["1111", 1, 3], ["2211", 2, 2], ["3210", 4, 0]])
    
    # Exercise 4
    code_attempts = []
    attempt_1 = ["4000", 0, 1]
    attempt_2 = ["4012", 2, 1]
    attempt_3 = ["0412", 3, 0]
    code_attempts = code_attempts + [attempt_1]
    code_attempts = code_attempts + [attempt_2]
    code_attempts = code_attempts + [attempt_3]
    if has_attempts_remaining(code_attempts, 1000) != "Not implemented yet":
        print("Testing exercise 4...")
        success = True
        if not has_attempts_remaining(code_attempts, 10):
            success = False
            print("--- Test 4-A failed.")
        if has_attempts_remaining(code_attempts, 2):
            success = False
            print("--- Test 4-B failed.")
        attempt_4 = ["5412", 4, 0]
        code_attempts = code_attempts + [attempt_4]
        if not has_attempts_remaining(code_attempts, 10):
            success = False
            print("--- Test 4-C failed.")
        if has_attempts_remaining(code_attempts, 3):
            success = False
            print("--- Test 4-D failed.")
        if has_attempts_remaining(code_attempts, 4):
            success = False
            print("--- Test 4-E failed.")
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
    
    # Exercise 5
    code_attempts = []
    attempt_1 = ["4000", 0, 1]
    attempt_2 = ["4012", 2, 1]
    attempt_3 = ["0412", 3, 0]
    attempt_4 = ["5412", 4, 0]
    code_attempts = code_attempts + [attempt_1]
    code_attempts = code_attempts + [attempt_2]
    code_attempts = code_attempts + [attempt_3]
    code_attempts = code_attempts + [attempt_4]
    if is_game_won(code_attempts) != "Not implemented yet":
        print("Testing exercise 5...")
        success = True
        if not is_game_won(code_attempts):
            success = False
            print("--- Test 5-A failed.")
        attempt_5 = ["5410", 3, 0]
        code_attempts = code_attempts + [attempt_5]
        if is_game_won(code_attempts):
            success = False
            print("--- Test 5-B failed. Only check if the last attempt in the list is the correct code.")
        code_attempts = []
        if is_game_won(code_attempts):
            success = False
            print("--- Test 5-C failed.")
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
    
    # Exercise 6a
    if any_digit_exceeds_highest_digit_value("0", 0) != "Not implemented yet":
        print("Testing exercise 6a...")
        success = True
        if any_digit_exceeds_highest_digit_value("0", 3):
            success = False
            print("--- Test 6a-A failed.")
        if any_digit_exceeds_highest_digit_value("4344", 4):
            success = False
            print("--- Test 6a-B failed.")
        if not any_digit_exceeds_highest_digit_value("2987778", 7):
            success = False
            print("--- Test 6a-C failed.")
        if not any_digit_exceeds_highest_digit_value("02159", 6):
            success = False
            print("--- Test 6a-D failed.")
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
    
    # Exercise 6b
    if contains_only_numbers("0") != "Not implemented yet":
        print("Testing exercise 6b...")
        success = True
        if not contains_only_numbers("0"):
            success = False
            print("--- Test 6b-A failed.")
        if not contains_only_numbers("990087654123"):
            success = False
            print("--- Test 6b-B failed.")
        if contains_only_numbers("O0431"):
            success = False
            print("--- Test 6b-C failed.")
        if contains_only_numbers("79 72 04"):
            success = False
            print("--- Test 6b-D failed.")
        if contains_only_numbers("1234+"):
            success = False
            print("--- Test 6b-E failed.")
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
            
    # Exercise 6c
    if is_valid_code_guess("0", 1, 1) != "Not implemented yet":
        print("Testing exercise 6c...")
        success = True
        if not is_valid_code_guess("0", 1, 4):
            success = False
            print("--- Test 6c-A failed.")
        if not is_valid_code_guess("990087654123", 12, 9):
            success = False
            print("--- Test 6c-B failed.")
        if is_valid_code_guess("O0431", 5, 6):
            success = False
            print("--- Test 6c-C failed.")
        if is_valid_code_guess("79 72 04", 8, 9):
            success = False
            print("--- Test 6c-D failed.")
        if is_valid_code_guess("1234+", 5, 5):
            success = False
            print("--- Test 6c-E failed.")
        if not is_valid_code_guess("4344", 4, 4):
            success = False
            print("--- Test 6c-F failed.")
        if is_valid_code_guess("2987778", 7, 7):
            success = False
            print("--- Test 6c-G failed.")
        if is_valid_code_guess("02159", 5, 6):
            success = False
            print("--- Test 6c-H failed.")
        if is_valid_code_guess("", 1, 9):
            success = False
            print("--- Test 6c-I failed.")
        if is_valid_code_guess("0332", 5, 9):
            success = False
            print("--- Test 6c-J failed.")
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
    
    # Exercise 7
    if generate_code(4, 4) != "Not implemented yet":
        print("Testing exercise 7...")
        success = True
        
        for i in range(0, 3):
            first_code = generate_code(i+4, i+5)
            always_same_code = True
            j = 0
            while j < 10:
                generated_code = generate_code(i+4, i+5)
                if first_code != generated_code:
                    always_same_code = False
                if len(generated_code) != i+4:
                    success = False
                    print("--- Test 7 failed. Generated code is not a string with the correct number of digits.")
                    break
                count_list = []
                k = 0
                while k < 10:
                    count_list = count_list + [0]
                    k = k + 1
                for element in generated_code:
                    if not element in "0123456789":
                        success = False
                        print("--- Test 7 failed. Generated code does not contain numbers only.")
                        break
                    count_list[int(element)] = count_list[int(element)] + 1
                for total in count_list:
                    if total > 1:
                        print("--- Test 7 failed. All digits of the generated code must be unique.")
                        success = False
                        break
                j = j + 1
                if not success:
                    break
            if always_same_code:
                success = False
                print("--- Test 7 failed. The generated code is not random.")
            if not success:
                break
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")

    # Exercise 8
    if get_hint("0") != "Not implemented yet":
        print("Testing exercise 8...")
        success = True
        
        result = get_hint("120")
        if result != "1XX" and result != "X2X" and result != "XX0":
            success = False
            print("--- Test 8-A failed. Returned string is incorrect.")
        always_same_result = True
        for i in range(0,10):
            if result != get_hint("120"):
                always_same_result = False
        if always_same_result:
            success = False
            print("--- Test 8-A failed. Returned string is not random.")
        
        result = get_hint("5034")
        if result != "5XXX" and result != "X0XX" and result != "XX3X" and result != "XXX4":
            success = False
            print("--- Test 8-B failed. (Returned string is incorrect.)")
        always_same_result = True
        for i in range(0,10):
            if result != get_hint("5034"):
                always_same_result = False
        if always_same_result:
            success = False
            print("--- Test 8-B failed. (Returned string is not random.)")
    
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
            
    # Exercise 9
    if compare("0", "0") != "Not implemented yet":
        print("Testing exercise 9...")
        success = True
        if compare("0", "0") != ["0", 1, 0]:
            success = False
            print("--- Test 9-A failed.")
        if compare("1111", "3201") != ["1111", 1, 3]:
            success = False
            print("--- Test 9-B failed.")
        if compare("531", "153") != ["531", 0, 3]:
            success = False
            print("--- Test 9-C failed.")
        if compare("90210", "90210") != ["90210", 5, 0]:
            success = False
            print("--- Test 9-D failed.")
        if compare("1155", "1253") != ["1155", 2, 2]:
            success = False
            print("--- Test 9-E failed.")
        if success:
            print(">>> Success - 1/1")
            score = score + 1
        else:
            print(">>> Fail - 0/1")
            
    return score

if __name__ == "__main__":
    print("Score: " + str(test_code()) + "/9")

################################################################################
# Additional functions. Not part of the exercises, but required to run the game.
################################################################################

def ask_input(code_attempts, max_attempts):
    """Print a request that the player has to input a code, and return the player's input.

    Parameters:
    code_attempts (list) -- Contains all player's attempts.
    max_attempts (int) -- The maximum number of attempts allowed.
    """
    message = "Attempt " + str(len(code_attempts)+1) + "."
    random_number = random.randint(0, 2)
    random_messages = []
    if len(code_attempts)+1 < max_attempts/2:
        random_messages.append("Try to guess the correct code.")
        random_messages.append("Can you find the code?")
        random_messages.append("What's your guess?")
    else:
        random_messages.append("Not many attempts left. Will you crack the code?")
        random_messages.append("Only " + str(max_attempts-len(code_attempts)) + " left.")
        random_messages.append("You're getting closer to the solution. Make each try count.")
    print(message + " " + random_messages[random_number])
    return input()

def show_objective(number_of_digits, highest_digit_value, max_attempts):
    """Print the game rules.

    Parameters:
    number_of_digits (int) -- The number of unique digits the code should have.
    highest_digit_value (int) -- The highest value that is allowed for any digit of the code.
    max_attempts (int) -- The maximum number of attempts allowed.
    """
    time.sleep(1)
    print_separator()
    print("Objective:")
    print("Find the " + str(number_of_digits) + "-digit code in at most " + str(max_attempts)
          + " attempts. All digits are between 0 and "
          + str(highest_digit_value) + " (both included).")
    print_separator()
    time.sleep(1)

def show_feedback(nb_of_correct_digits, nb_of_digits_in_wrong_position):
    """Print feedback on the player's guess.

    Parameters:
    nb_of_correct_digits (int) -- The number of correct digits the player's code has at the correct position.
    nb_of_digits_in_wrong_position (int) -- The number of wrongly placed correct digits in the player's code.
    """
    print("- Correct digits at correct position: " + str(nb_of_correct_digits))
    print("- Correct digits at wrong position: " + str(nb_of_digits_in_wrong_position))

def show_win_conditionally(cheated, hints_needed):
    """Print a message to let the player know they used the cheat or hint command.

    Parameters:
    cheated (boolean) -- Contains true if the player used the cheat command.
    hints_needed (int) -- The number of times the players asked for a hint.
    """
    time.sleep(3)
    message = "...That would be the message you'd get to see here, but "
    if cheated:
        message = message + "you've cheated to win"
    if cheated and hints_needed > 0:
        message = message + ", and "
    if hints_needed > 0:
        message = message + "you've asked for a hint " + str(hints_needed) + " time"
    if hints_needed > 1:
        message = message + "s"
    message = message + ". As a result, your score remains unchanged."
    print(message)
    time.sleep(3)

def show_lose_message(correct_code):
    """Print a message to inform the player that they've lost.

    Parameters:
    correct_code (string) -- The code the player had to guess.
    """
    print("Too bad! No more attempts left. The correct code was " + correct_code + ".")

def show_reward_code_length_increased():
    """Print a message to inform the player that the code length is increased by one digit."""
    time.sleep(2)
    print("The length of the code is now increased by one digit!")

def show_reward_digit_value_cap_increased():
    """Print a message to inform the player that the highest possible value of each digit is increased."""
    time.sleep(2)
    print("The highest possible value of each digit is now increased by one!")

def show_reward_attempts_increased():
    """Print a message to inform the player that they gained to additional attempts from next game on."""
    time.sleep(2)
    print("You get two additional attempts in your next game!")

def show_score(score):
    """Print the player's score.

    Parameters:
    score (int) -- The player's current score.
    """
    time.sleep(1)
    print("Score: " + str(score))

def show_hint(hint):
    """Print the given hint.

    Parameters:
    hint (string) -- The hint to print.
    """
    print_separator()
    print("Hint: " + hint)
    print_separator()

def show_invalid():
    """Print a message to inform the player that their input is invalid."""
    print_separator()
    print("The code or command you've entered is invalid.")
    print_separator()

def show_game_header():
    """Print the header with the title of the game."""
    print("=====================")
    print("||   MASTERMIND+   ||")
    print("=====================")

def print_separator():
    """Print a separator to make all text appearing on screen more readable/structured."""
    print("---------------------")
