# alter the code so that it does what it should do

age = 10

if age < 18 and age > 0:
    message = "je bent minderjarig"
elif age >= 18:
    message = "je bent meerderjarig"
else:
    message = "error - age < 0"
    
print(message)