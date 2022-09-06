user = "admin"
key = 1234

def loginsection():
    userName = input("Username :")
    passWord = int(input("Password :"))
    if userName == user and passWord == key:
        showmenu()
    else:
        loginsection()

def showmenu():
    print("What you want to do?")
    print("1. Vat calculator")
    print("2. Price calculator")
    userSelect = int(input(">> "))
    return menuselect(userSelect)

def menuselect(userSelect):
    while userSelect != 0:
        if userSelect == 1:
            totalPrice = float(input("Price : "))
            return vatcalculate(totalPrice)
        elif userSelect == 2:
            return pricecalculate()
        else:
            print("Try again")
            showmenu()
    else:
        print("Done")
        exit()

def vatcalculate(totalprice):
    vat = 7
    result = (totalprice + (totalprice * vat / 100))
    print(result)

def pricecalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalprice = price1 + price2
    return vatcalculate(totalprice)

loginsection()
