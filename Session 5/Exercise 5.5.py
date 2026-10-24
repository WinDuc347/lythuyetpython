import math

def table():
    width = 4
    height = 1
    while width*height >= 0.49:
        print(round(width * height, 2), " for width = ", round(width, 2), " and height = ", round(height, 2))
        width -= 0.1
        height += 0.1
table()