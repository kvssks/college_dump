def mat():
    i = int(input("row:\n>"))
    j = int(input("col:\n>"))
    arr = [[int(input(">")) for x in range(j)]for y in range(i)]
    return arr
def Mprint(mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(row):
        print("|",end=" ")
        for j in range(col):
            print(mat[i][j],end=" ")
        print("|")
def transp(mat):
    row = len(mat[0])
    col = len(mat)
    arr = [[mat[x][y] for x in range(col)]for y in range(row)]
    return arr
def det(mat):    
    row = len(mat)
    col = len(mat[0])
    det = 0
    for j in range(col):
        det += mat[0][j]*(mat[1][j+1]*mat[-1][j-1]-mat[1][j-1]*mat[-1][j+1])
    return det
k = mat()
# Mprint(k)
# Mprint(transp(k))
print(det(k))