productList = {"Mouse":3000, "Keyboard":5000, "Monitor":15000, "Headphone":10000}
userList = []
userPrice = []
def login():
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")
    if usernameInput == "Lek" and passwordInput == "12345":
        return showMenu()
    else:
        print("error")
def showMenu():
    print("Seller:","Welcome :)")
    print("Seller:","This is our product")
    print(productList)
    print("Seller:","What would you like to buy?")
    return menuSelect()
def menuSelect():
    while True:
        userSelect = input("Customer: ")
        if userSelect in productList.keys():
            menuPrice = int(input("Price: "))
            userList.append(userSelect)
            userPrice.append(menuPrice)
        else:
            break
    return priceCalculator()

def priceCalculator():
    for number in range(len(userList)):
        print(userList[number], userPrice[number])
    Summary = sum(userPrice)
    return vatCalculator(Summary)

def vatCalculator(Summary):
    vat = 7
    vatCalculator = print(Summary+(Summary*vat)/100)

login()
