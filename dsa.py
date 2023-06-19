# s = input()
# l1 = len(s)
# kk = []
# for i in range(l1):
#     if s[i]=="[":
#         k = []
#         l = ''
#         for j in range(i+1,l1):
#             if s[j]==",":
#                 k.append(int(l))
#                 l = ''
#                 continue
#             elif s[j]=="]":
#                 i = j
#                 break
#             else:
#                 l = l+s[j]
#         if (len(k)>0):
#             kk.append(k)
# print("kk=",kk)


s = input()
l = len(s)
k = []
for i in range(1,l):
    a = []
    b = ''
    if s[i]=="[":
        for j in range(i+1,l):
            if(s[j]=="]"):
                a.append(int(b))
                i = j+1
                break
            elif(s[j]==","):
                a.append(int(b))
                b = ''
                continue
            else :
                b = b+s[j]
    if (len(a)>0):
        k.append(a)
print("k=",k)
# # print(len(k[1]))
# max = 0
# min = 0 
# for i in k:
#     # print(i)
#     if(len(k[max])<len(i)):
#         max = k.index(i)
#     if(len(k[min])>len(i)):
#         min = k.index(i)
# print(max,len(s[max]),s[max])
# print(min,len(s[min]),s[min])