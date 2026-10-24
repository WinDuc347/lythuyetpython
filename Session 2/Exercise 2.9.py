# ex9.1
floor = int(input("floor number "))
if floor < 0:
    print("error - too low")
elif floor > 60:
    print("error - too high")
elif floor == 0 or floor == 60:
    print("DING!")
elif floor%10 == 0:
    print(floor)
else:
    print("...")
    


#  ex9.2
floor = int(input("floor number "))
max_floor = 1000
if floor < 0:
    print("error - too low")
elif floor > max_floor:
    print("error - too high")
elif floor == 0 or floor == max_floor:
    print("DING!")
elif floor%10 == 0:
    print(floor)
else:
    print("...")