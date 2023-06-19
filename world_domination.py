def password():
    p = ""
    s = "!@#$%^&*"
    n = "1234567890"
    while(True):
        print("enter a password")
        p = input()
        if("A">p[0] or p[0]>"Z"):
            print("password should start with a CAPITAL letter")
            continue
        if(len(p)>15 or len(p)<8):
            print("your password should contain 8 to 15 characters ")    
            continue
        sc = 0 
        nc = 0 
        for i in p:
            if (i in s):
                sc+=1
            if (i in n):
                nc+=1
        if(sc==0 or nc==0):
            print("password should contain atleast 1 special character and a number")
            continue
        return p
def reg():
    l = []
    # while(True):
    user = input("enter your user name : ")
    name_first = input("enter your first name : ")
    name_last = input("enter your last name : ")
    passs = password()
    l.append(user)
    l.append(passs)
    l.append(name_first)
    l.append(name_last)
    l.append(int(input("enter your phone number: ")))
    l.append(input("enter your email id : "))
    return l
def log(l):
    name = input("enter your user name")
    passW = input("enter your password")
    ref = 0 
    for i in range(0,len(l)):
        if (name == l[i][0]):
            ref = i 
            break
    c = 0 
    while(c<=3):
        if(passW == l[ref][1]):
            print("logged in successfully :)")
            return True
        else :
            print("wrong password \n you have ",3-c," more chances left ")
            c+=1
            passW = input("enter your password")
    if(c==3):
        print("you have been busted , FBI is on the way ")
        return False
cons = "Yes"
database = []
while(cons=="Yes" or cons =="Y" or cons == "y" or cons == "yes"):
    i = int(input("choose an option \n 1:sign up \n 2:login\n >"))
    if(i==1):
        database.append(reg())
    elif(i==2):
        if(log(database)==True):
            print("login successful")
        else:
            print("login failed")
    else :
        print("please enter a valid option")
    cons = input("do you want to continue")
