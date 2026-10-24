#draw block structures + predict output
a = -4
b = 7
c = 6

if a > 0:
    if b == 7:
        c = c + 1
    elif b == 8:
        if c < 0:
            c = 0
        else:
            c = a + b
else:
    a = 0
    if c < 0:
        d = "c is negative"
    elif c == 0:
        d = "c is zero"
    else:
        d = "c is positive"
        if c < 10:
            d = d + " , but smaller than 10"
            if c%2 == 0:
                d = d + " and even"
            if c%3 == 0:
                d = d + " and divisible by 3"
            else:
                d = d + " and not divisible by 3"                              
if a == 0: 
    c = 100
    a = -a
b = 200

print("a:",a,"b",b,"c:",c,"d:",d)