Income = 0
Expanses = []

def Display_Menu():
    print("\n 1. Add Income")
    print("2 . Add Expanse")
    print("3 . Show Balance")
    print("4 . Exit")



def Add_Income():
    global Income
    Amt = float(input("Enter amount : "))
    Income += Amt



def Add_Expanses():
    global Expanses
    Name = input("Enter Product Name : ")
    Amt = float(input("Enter a Product Amount : "))
    Expanses.append((Name , Amt))



def Show_Balance():
    Total_Expanses = sum([e[1] for e in Expanses])
    print(f"\n Income :  {Income} ")
    print(f"Expanses : {Total_Expanses}")
    print(f"Balance : {Income - Total_Expanses}")



while True:
    Display_Menu()
    Choice = input ("Enter Choice : ")
    if Choice == "1":
        Add_Income()
    elif Choice == "2":
        Add_Expanses()
    elif Choice == "3":
        Show_Balance()
    elif Choice == "4":
        break
    else:
        print("Invalid Choice")


