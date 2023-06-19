# n = int(input("enter a number \n >"))
# while(n>=10):
#     s = 0 
#     while(n>0):
#         s+=n%10
#         n//=10
#     n = s
#     print("step=",n)
# print(n)
# 
# 
# def is_prime(n):
#     if(n%2==0):
#         # print("1")
#         return False
#     else :
#         for i in range(3,int(n/2)+1,2):
#             # print(i)
#             if (n%i==0):
#                 # print("2",n,i)
#                 return False 
#     return True
# print(is_prime(int(input())))
# 
# 
# def rev_no(n):
#     rev = 0 
#     while(n>0):
#         rev+=n%10
#         n//=10
#     return rev
# 
# 
n = int(input("enter a number"))
s = []
while(n>0):
    if(n==1):
        print("yes")
        break
    l = 0
    while(n>0):
        l += (n%10)**2
        n//=10
    n = l
    if (n in s):
        print ("no")
        break
    s.append(n)