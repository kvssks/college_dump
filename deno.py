n = int(input('enter the amount\n>'))
l = [500,200,100,50,20]
c = [0,0,0,0,0]
i  = 0 
while(i<len(l)):
    if(l[i]>n):
        i+=1
    else:
        n-=l[i]
        c[i]+=1
for j in range(len(l)):
    print("number of",l[j],"notes is ",c[j])
print("remaining change is ",n)