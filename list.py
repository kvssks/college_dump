x = int(input())
y = int(input())
z = int(input())
n = int(input())
print(x,y,z)
list = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if(i != n and j != n and k != n) ]
print(list)