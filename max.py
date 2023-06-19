max = int(input())
try:
    while(True):
        i = input()
        if(int(i)>max):
            max = int(i)
except:
    print("the maximum number is ",max)