import Mastermind_Test
import random


######################################
# DO NOT CHANGE ANYTHING IN THIS FILE.
######################################

###################
# Global variables.
###################

number_of_digits = 4
highest_digit_value = 5
max_attempts = 10
score = 0
correct_code = ""
code_attempts = []
hints_needed = 0
cheated = False

##################################
# Main program (flow of the game).
##################################

if Mastermind_Test.test_code() != 9:
    print("COMPLETE ALL FUNCTIONS FIRST. ONLY TRY TO RUN THE GAME WHEN ALL TESTS PASS.")
    exit()

Mastermind_Test.show_game_header()
while True:
    code_attempts = []
    hints_needed = 0
    cheated = False
    correct_code = Mastermind_Test.generate_code(number_of_digits, highest_digit_value)
    Mastermind_Test.show_score(score)
    Mastermind_Test.show_objective(number_of_digits, highest_digit_value, max_attempts)
    playing = True
    while playing:
        while not Mastermind_Test.is_game_won(code_attempts) and Mastermind_Test.has_attempts_remaining(code_attempts, max_attempts):
            user_input = Mastermind_Test.ask_input(code_attempts, max_attempts)
            if Mastermind_Test.is_valid_code_guess(user_input, number_of_digits, highest_digit_value):
                attempt = Mastermind_Test.compare(user_input, correct_code)
                code_attempts = code_attempts + [attempt]
                if attempt[1] < number_of_digits:
                    Mastermind_Test.show_feedback(attempt[1], attempt[2])
            else:
                if user_input.lower() == "hint":
                    Mastermind_Test.show_hint(Mastermind_Test.get_hint(correct_code))
                    hints_needed = hints_needed + 1
                elif user_input.lower() == "cheat":
                    Mastermind_Test.show_correct_code(correct_code)
                    cheated = True
                elif user_input.lower() == "attempts":
                    Mastermind_Test.show_all_attempts(code_attempts)
                else:
                    Mastermind_Test.show_invalid()
        if Mastermind_Test.is_game_won(code_attempts):
            Mastermind_Test.show_win_message(code_attempts)
            if hints_needed > 0 or cheated:
                Mastermind_Test.show_win_conditionally(cheated, hints_needed)
            else:
                score = score + 1
                random_number = random.randint(0, 1)
                if random_number == 0 and highest_digit_value < 9:
                    highest_digit_value = highest_digit_value + 1
                    Mastermind_Test.show_reward_digit_value_cap_increased()
                elif random_number == 1 and number_of_digits < highest_digit_value:
                    number_of_digits = number_of_digits + 1
                    Mastermind_Test.show_reward_code_length_increased()
                max_attempts = max_attempts + 2
                Mastermind_Test.show_reward_attempts_increased()
            playing = False
        elif not Mastermind_Test.has_attempts_remaining(code_attempts, max_attempts):
            Mastermind_Test.show_lose_message(correct_code)
            playing = False
