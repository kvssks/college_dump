f1 = input("Enter the name of the first fruit:")
f2 = input("Enter the name of the second fruit:")
for i in range(min(len(f1),len(f2))):
    if(i==min(len(f1),len(f2))-1):
        print(f1,"and",f2,"are the same.")
    elif(f1[i]==f2[i]):
        continue
    elif(f1[i]>f2[i]):
        print(f1,"comes after",f2,"in the dictionary")
        break
    else:
        print(f1,"comes before",f2,"in the dictionary")
        break