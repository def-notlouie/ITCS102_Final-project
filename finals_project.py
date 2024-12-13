def activity1():
    pass
def activity2():
    pass
def activity3():
    x = eval(input("enter a number: "))
    y = eval(input("enter a number: "))
    z = x + y
    print(f"the sum of {x} and {y} is {z}")


def activity4():
    x = 5
    print(x)
    x += 10
    print(x)
    x += 15
    print(x)
    x += 20
    print(x)





def activity5():

    for a in range (11, 0 , -1):
        for b in range (11, a, -1):
            print(" ",end="")
    print("*" *a)

def activity6():
    for x in range (6,1,-1):
        for a in range (x,1,-1):
            print(" ", end=" ")
        for b in range (x,7,1):
            print("*",end=" ")
        for c in range (x,6,1):
            print("*", end=" ")
        print()

    for x in range (1,7):
        for a in range (1,x,1):
            print(" ", end=" ")
        for b in range (7, x, -1):
            print("*",end=" ")
        for c in range (6, x, -1):
            print("*", end=" ")
        print()
def activity7():
    A = {}

    def accs():
        v = input("enter user:")
        if v in A:
            print("this account is already exist")
            
        else:
            A[v] = 0
            print(f"the account was already created for {v}")
            
    # def acc_main(): 
    #     while True:
    #         print("type new for creation of account")
    #         x = input("enter a command:")
    #         if x == "new":
    #             accs()           
    # acc_main()

    
def activity8():
    pass
def activity9():
    pass
def activity10():
    pass
def activity11():
    pass
def activity12():
    pass
def activity13():
    pass
def activity14():
    pass
def activity15():
    pass
def activity16():
    pass
def activity17():
    pass
def activity18():
    pass
def activity19():
    pass
def activity20():
    pass
def activity21():
    pass
def activity22():
    pass
def activity23():
    pass
def activity24():
    pass
def activity25():
    pass

def main():
    while True:
        coms = input("Enter an instruction: ")
        if coms.lower() == "exit":
            break
            print("program terminated")
        elif coms.lower() == "cat1":
            activity1()
            continue
        elif coms.lower() == "cat2":
            activity2()
            continue
        elif coms.lower() == "cat3":
            activity3()
            continue
        elif coms.lower() == "cat4":
            activity4(coms)
            continue
        elif coms.lower() == "cat5":
            activity5()
            print("program executed")
            continue
        elif coms.lower() == "cat6":
            activity6()
            print("program executed")
            continue
        elif coms.lower() == "bank":
            activity7()
            print("programm terminated")
        elif coms.lower() == "cat8":
            activity8()
            continue
        elif coms.lower() == "cat9":
            activity9()
            continue
        elif coms.lower() == "cat10":
            activity10()
            continue
        elif coms.lower() == "cat2":
            activity11()
            continue
        elif coms.lower() == "cat2":
            activity12()
            continue
main()