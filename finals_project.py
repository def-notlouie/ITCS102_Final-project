user_data = {}

def hello_world(x):
    print(f"hello {x}, do you know that printing 'hello world' in python is very common in programming")
    print("Hello world")
    print()
    print("**print()** is a built in function in python, just insert quotation marks inside the the parentheses("")")


def activity2(x):
    
    y = input("enter your age : ")
    z = input("enter your hobby : ")
    yy = input("enter your goals : ")
    print()
    print(f"hello my name is {x}, and I'm {y} years old. my favorite hobby is {z}, and the goal i root the most is {yy}")
    print()

def activity3():
    x = eval(input("enter a number: "))
    y = eval(input("enter a number: "))
    z = x + y
    print(f"the sum of {x} and {y} is {z}")
    print()

def activity4():
    x = 5
    print(x)
    x += 10
    print(x)
    x += 15
    print(x)
    x += 20
    print(x)
    print()





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

def activity7(accs):
    A = {}

    def accs(v):
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
    

    

# Function to create a new user
def create_user():
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists. Please choose another.")
        return
    password = input("Enter a password: ")
    user_data[username] = password
    print("User created successfully!")

# Function to log in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_data.get(username) == password:
        print()
        print(f"Login successful! Welcome,   {username}  !")
    else:
        print("Invalid username or password.")

    # Menu loop
    


    # if password.lower() == "": 
    #     print("Access Granted")
    #     print("Enjoy using the system")
    # elif password.lower() == "1004":
    #     print("Welcome, Yoon Jeonghan")
    #     print("Access Granted")
    # else:
    #     print("Incorrect password, Access Denied")
    # print("Thank you!")

    # x = int(input("enter a temperature"))
    # if x <= 20:
    #     print("it is cold ain't it?")
    # elif x <= 25:
    #     print("it's moderate temp")
    # elif x <= 30:
    #     print("it is hot today ain't it")
    # elif x <= 35:
    #     print("bro it's super hot, you're slowly cooking")
    
def activity9():
    pass
def activity10():
    name = input("Enter Your Name: ")

    isStudent = input("Are you a student of DLL(Yes/No): ")

    if isStudent.lower()=="yes":
        print("Welcome to the DLL BSIT Scholarship form") 
        GG = input("Are you from Brgy. Silangang mayao? (yes/no):")
        if GG.lower()=="yes":
            print("Please fillup the second form")
            yearlevel = input("What year are you currently enrolled?\nF-Freshnen\nS-Sophomore\nJ-Junior\nR-Senior\nPlease input your answer here: ")

            if yearlevel.lower() == 'f':
                print(f"Hi {name}, Freshmen, Welcome to DLL")

            elif yearlevel.lower() == 's': 
                print(f"Hi {name}, Sophomore, Welcome to DLL")

            elif yearlevel.lower() == 'j': 
                print(f"Hi {name}, Junior, Welcome to DLL")

            elif yearlevel.lower() == 'r': 
                print(f"Hi {name}, Senior, Welcome to DLL")

            else:
                print("Invalid Option")
            IsNeeded = input("Would you like to apply for a scholarship? (yes/no): ")

            if IsNeeded.lower() == "yes":
                print("Scholarship approved")
            else:
                print("Unfortunately, this scholarship grant are only for residents of Silangan Mayao only")
            print("Your form has been successfully submitted")
            print()
    
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
def bato_bato_pick():
    x = input("enter a guess: ")
    

def main():
    while True:
        print("louie's finals project on  ITCS102")
        coms = input("Enter an instruction: ")
        if coms.lower() == "exit":
            print("program terminated")
            break
        else:
            if coms.lower() == "cat1":
                x = input("what's you're name?------>")
                hello_world(x)
                continue
            elif coms.lower() == "cat2":
                x = input("enter your name: ")
                activity2(x)
                continue
            elif coms.lower() == "cat3":
                activity3()
                continue
            elif coms.lower() == "cat4":
                activity4(coms)
                continue
            elif coms.lower() == "cat5":
                do
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
                def mainpass():
                    while True:
                        print("\n1. Create User")
                        print("2. Login")
                        print("3. back to main dash board")
                        choice = input("Choose an option: ")
                        if choice == "1":
                            create_user()
                        elif choice == "2":
                            login()
                        elif choice == "3":
                            print(f"Goodbye!")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                mainpass()
                
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