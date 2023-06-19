def amean(x):
    l = len(x)
    s = 0
    for i in x:
        s+=i
    return s/l
def gmean(x):
    l = len(x)
    s = 1 
    for i in x:
        s*=i
    return(s**(1/l))
def hmean(x):
    l = len(x)
    s = 0
    for i in x:
        s+=(i)**(-1)
    return (l/s)
print("enter the numbmbers ")
k =list( map(int,input().split()))
print(hmean(k))
