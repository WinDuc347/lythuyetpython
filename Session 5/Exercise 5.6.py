import random

number = random.randint(0, 100)

for i in range(6):
    guess = int(input("Input the number: "))
    
    if guess > number:
        print("Too big, still have ", 5 - i, " times to guess.")
    elif guess < number:
        print("Too small, still have ", 5 - i, " times to guess.")
    else:
        print("Congrats, correct guess!")
        break
fo