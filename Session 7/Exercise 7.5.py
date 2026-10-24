def matrix_multiplication(matrix1,matrix2):
    result = []
    
    if len(matrix1[0]) != len(matrix2):
        return result
    
    for i in range(len(matrix1)):
        row = []
        
        for j in range(len(matrix2[0])):
            total = 0
            
            for k in range(len(matrix1[0])):
                total += matrix1[i][0+k]*matrix2[0+k][j]
            
            row.append(total)
            
        result.append(row)
        
    return result



#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
m1 = [[0,1,8],[-7,5,1]]
m2 = [[8,0],[4,4],[1,8]]
m3 = [[1,0,1]]
m4 = [[7],[-8],[9]]

m1m2 = matrix_multiplication(m1,m2)
m2m1 = matrix_multiplication(m2,m1)
m3m4 = matrix_multiplication(m3,m4)
m4m3 = matrix_multiplication(m4,m3)

if m1m2 == [[12, 68], [-35, 28]] and m2m1 == [[0, 8, 64], [-28, 24, 36], [-56, 41, 16]] and m3m4 == [[16]] and m4m3 == [[7, 0, 7], [-8, 0, -8], [9, 0, 9]]:
    print("Matrix product calculated correctly")
else:
    print("Wrong result")
