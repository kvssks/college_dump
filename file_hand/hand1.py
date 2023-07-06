f = open("emp.txt","r")
l = f.readlines()
k = []
for i in l:
    k.append(i.split(","))
for i in range(len(k)):
    k[i][-1]=int(k[i][-1])
# print(k)
f2 = open("ep.txt","w")
leng = len(k)
for i in range(leng):
    gret=0
    p=k[0]
    for j in k:
        if(gret<j[-1]):
            gret=j[-1]
            p = j
    # f2.write(str(p))
    for q in p:
        f2.write(str(q))
        f2.write(",")
    f2.write("\n")
    k.remove(p)