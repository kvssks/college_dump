def suml(l):
    s = 0
    for i in l:
        s+=i
    return (s/len(l))

d={input("enter your rollnumber"):[int(input("enter your marks : ")) for i in range(3)] for j in range(1,3)}
for i in d:
    print(i,"=",suml(d[i]))
    # print(d[i])