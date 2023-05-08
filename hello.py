# string = "hello world"
# len = len(string)
# pos_vow = 0
# vow = ['a','e','i','o','u']
# for i in range(len):
#     if(string[i] in vow ):
#         pos_vow = i
#         while(string[pos_vow]!=" "):
#             print(string[pos_vow],end="")
#             pos_vow+=1
#             if(pos_vow==len):
#                 break
#         print()
str="Hello world"
for i in range(0,len(str)):
    if(str[i]!=" "):
        if(str[i]=='a'or str[i]=='e'or str[i]=='i'or str[i]=='o'or str[i]=='u'):
            j=i
            while(str[j]!=" "):
                print(str[j],end="")
                j+=1
            print()