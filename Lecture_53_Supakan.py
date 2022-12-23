def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
totalPrice = int(input("totalPrice: "))
print("Summary= ",vatCalculate(totalPrice))