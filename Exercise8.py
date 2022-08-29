userName = input("Enter Username :")
passWord = input("Enter Password :")

if userName == "admin" and passWord == "admin":
    print("Welcome to our shop")
    print("1.Banana   : 30THB")
    print("2.Apple    : 10THB")
    print("3.Orange   : 15THB")
    print("What would you like to buy?")
    userSelected = int(input(">> "))
    if userSelected == 1:
        userSelected = 30
    elif userSelected == 2:
        userSelected = 10
    elif userSelected == 3:
        userSelected = 15
    amount = int(input("Amount >> "))
    print("Do you want anything else?")
    userChoice = input("Yes/No >> ")

    if userChoice == "yes" or userChoice == "Yes":
        print("What do you want?")
        print("1.Banana   : 30THB")
        print("2.Apple    : 10THB")
        print("3.Orange   : 15THB")
        userSelected2 = int(input(">> "))
        if userSelected2 == 1:
            userSelected2 = 30
        elif userSelected2 == 2:
            userSelected2 = 10
        elif userSelected2 == 3:
            userSelected2 = 15
        amount2 = int(input("Amount >> "))
        print("----RECEIPT----")
        print(userSelected, "*", amount, ":", userSelected * amount)
        print(userSelected2, "*", amount2, ":", userSelected2 * amount2)
        print("Total :", (userSelected * amount) + (userSelected2 * amount2))

    elif userChoice == "no" or userChoice == "No":
        print("----RECEIPT----")
        print(userSelected, "*", amount, ":", userSelected * amount)
else:
    print("Error")
