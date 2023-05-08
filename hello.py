# creation of matrix functions 
def makeMatrix():
    row = int(input("Enter the number of elements of the row:"))
    col = int(input("Enter the number of elements of the col:"))
    matrix = [[int(input(">")) for j in range(col)] for i in range(row)]
    return matrix 
def printMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        print("[",end=" ")
        for j in range(col):
            print(matrix[i][j],end=" ")
        print("]")
def matMul(matrix1,matrix2):
    r1=len(matrix1)
    c1=len(matrix1[0])
    r2=len(matrix2)
    c2=len(matrix2[0])
    matrix = [[0 for f in range(c2)] for e in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                matrix[i][j]+=matrix1[i][k]*matrix2[k][j]
    return matrix
arr = makeMatrix()  
ar1 = makeMatrix()
printMatrix(matMul(arr,ar1))
