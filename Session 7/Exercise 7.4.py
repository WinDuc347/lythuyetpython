# Define matrix-printing function
def pretty_printer(matrix, separator):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = separator)
        print("")

# Read file and convert to matrix
def read_art_from_file(file_name):
    matrix = []
    
    file = open(file_name, "r")
    
    longest = len(max(open(file_name), key=len))
    
    for line in file:
        row = []
        
        line = line.rstrip()

        for i in range(len(line)):
            row.append(line[i])
            
        matrix.append(row)
    
    new_matrix = []
        
    for i in range(len(matrix)):
        row = []
        for j in range(longest):
            if j <= len(matrix[i]) - 1:
                row.append(matrix[i][j])
            else:
                row.append(" ")
                
        new_matrix.append(row)
        
    return new_matrix

## Test:
my_picture = read_art_from_file("ascii-art.txt")
pretty_printer(my_picture, "")



## Horizontal mirror filter:
def horizontal_mirror(picture):
    matrix = []
    for i in range(len(picture)):
        row = []
        for j in range(len(picture[i])):
            if picture[i][len(picture[i]) - j - 1] == "/":
                row.append("\\")
            elif picture[i][len(picture[i]) - j - 1] == "\\":
                row.append("/")
            elif picture[i][len(picture[i]) - j - 1] == ")":
                row.append("(")
            elif picture[i][len(picture[i]) - j - 1] == "(":
                row.append(")")
            elif picture[len(picture) - i - 1][j] == "`":
                row.append("'")
            else:
                row.append(picture[i][len(picture[i]) - j - 1])
        matrix.append(row)
    return matrix

## Test:
horizontal_pic = horizontal_mirror(my_picture)
pretty_printer(horizontal_pic, "")



## Shift picture left filter:
def left(picture, units):
    matrix = []
    for i in range(len(picture)):
        row = []
        for j in range(units, len(picture[i])):
            row.append(picture[i][j])
        matrix.append(row)
    return matrix

## Test:
left_pic = left(my_picture, 20)
pretty_printer(left_pic, "")



## Shift picture right filter:
def right(picture, units):
    matrix = []
    for i in range(len(picture)):
        row = []
        for j in range(len(picture[i]) - units):
            row.append(picture[i][j])
        matrix.append(row)
    return matrix

## Test:
right_pic = right(my_picture, 20)
pretty_printer(right_pic, "")



## Starry picture filter:
def starry(picture):
    matrix = []
    for i in range(len(picture)):
        row = []
        for j in range(len(picture[i])):
            if picture[i][j] != " ":
                row.append("*")
            else:
                row.append(" ")
        matrix.append(row)
    return matrix
## Test:
starry_picture = starry(my_picture)
pretty_printer(starry_picture, "")



## Vertical mirror filter:
def vertical_mirror(picture):
    matrix = []
    for i in range(len(picture)):
        row = []
        for j in range(len(picture[i])):
            if picture[len(picture) - i - 1][j] == "/":
                row.append("\\")
            elif picture[len(picture) - i - 1][j] == "\\":
                row.append("/")
            elif picture[len(picture) - i - 1][j] == "`":
                row.append("'")
            else:
                row.append(picture[len(picture) - i - 1][j])
        matrix.append(row)
    return matrix

## Test:
vertical_pic = vertical_mirror(my_picture)
pretty_printer(vertical_pic, "")