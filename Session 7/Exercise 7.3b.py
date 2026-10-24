def pretty_printer(matrix, separator):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = separator)
        print("")

def multiplication_tables(up_to_and_including):
    '''
    Construtcs matrix containing tables of multiplication (multiples of 1 to 10) up to given number
            Parameters:
                    up_to_and_including (int): number up to and including to which multiples have to be calculated
            Returns:
                    matrix (list of list(s)): matrix with as row i multiplication table of i, with up_to_and_including rows
    '''
    rows, columns = up_to_and_including, 10;
    
    matrix = [[0 for x in range(columns)] for y in range(rows)]
    
    for i in range(1, up_to_and_including+1):
        for j in range(1, 11):
            matrix[i-1][j-1] = i*j
        print("")
    
    return matrix

pretty_printer(multiplication_tables(5), "\t")

#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________

table = multiplication_tables(7)
if table == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]]:
    print("Multiplication tables generated correctly")
else:
    print("Wrong result")

