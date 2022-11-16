productList = ["Mouse", "Keyboard", "Monitor", "Headphone"]
productPrice = ["3000", "5000", "15000", "10000"]
def showproductList():
    print("1:",productList[0])
    print("2:",productList[1])
    print("3:",productList[2])
    print("4:",productList[3])
usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "lek" and passwordInput =="12345":
    print("Merchant: Welcome to computer shop")
    print("What would you like to order?")
    showproductList()
    customerInput = input("Customer: I would like to order ")
    if customerInput == "1":
        print(productList[0], productPrice[0])
        print("Merchant: How much do you need to order")
        customerselected = int(input("Total product: "))
        print("totalPrice=", customerselected*int(productPrice[0]))
        print("Thank you comes again (^_^)")
    elif customerInput == "2":
        print(productList[1], productPrice[1])
        print("Merchant: How much do you need to order")
        customerselected = int(input("Total product: "))
        print("totalPrice=", customerselected*int(productPrice[1]))
        print("Thank you comes again (^_^)")
    elif customerInput == "3":
        print(productList[2], productPrice[2])
        print("Merchant: How much do you need to order")
        customerselected = int(input("Total product: "))
        print("totalPrice=", customerselected*int(productPrice[2]))
        print("Thank you comes again (^_^)")
    elif customerInput == "4":
        print(productList[3], productPrice[3])
        print("Merchant: How much do you need to order")
        customerselected = int(input("Total product: "))
        print("totalPrice=", customerselected * int(productPrice[3]))
        print("Thank you comes again (^_^)")
else:
    print("Username or Password are incorrect, please try again")