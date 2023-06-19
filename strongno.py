def fact(n):
    f = 1 
    for i in range(1,n+1):
        f*=i
    return f
n = int(input("Enter a number "))
c = n 
s = 0
while(c>0):
    s += fact(int(c%10))
    print("the factorial =",fact(c%10))
    c//=10
if(s==n):
    print("strong")
else:
    print("not strong ")