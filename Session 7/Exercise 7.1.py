  my_matrix = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]]

#print(my_matrix[0][1])

#my_matrix[2][3] = 12

#print(my_matrix[2][3])

#my_matrix[0] = [2,1,8,-7]

#print (my_matrix[0])



def dimension(matrix):
    rows = 0
    columns = 0
    
    for i in range(len(matrix)):
        if rows == 0:
            for j in range(len(matrix[i])):
                columns += 1
        rows += 1
        
    
    dimension = [rows, columns]
    
    return dimension

print(dimension(my_matrix))