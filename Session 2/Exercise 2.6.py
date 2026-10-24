pi = 3.1
radius = 1
area = 2 * pi * radius

if pi >= 3.14:
    if radius < 0:
        print("error - negative radius")
    else:
        print(area)
else:
    print("error - pi not exact enough")
    