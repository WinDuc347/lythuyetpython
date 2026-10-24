my_matrix = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]]

def pretty_printer(matrix, separator):
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            print(matrix[i][j], end = separator)
        print("")


pretty_printer(my_matrix, "\t")