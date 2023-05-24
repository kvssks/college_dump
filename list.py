# for t in range(int(input())):
#     l = int(input())
#     a = list(map(int,input().split()))
#     a.sort()
#     c=0
#     m=1
#     m2=1
#     for i in a:
#         for j in a:
#             for k in a:
#                 m = j/i
#                 m2= k/j
#                 if ((j%i==0 and k%j==0)and(m==m2)and(id(i)!=id(j)!=id(k))):
#                     c+=1
#     print(c)
l = [[i for i in range(10)] for i in range(10)]
print(l[1][3:5])