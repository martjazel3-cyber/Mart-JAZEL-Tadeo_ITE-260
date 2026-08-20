print("============================")

name = input("Enter your name: ")

contact = input("Enter your Contact number: ")

address = input("Enter your address: ")


product1 = input("Enter product: ")

price1 = int(input("Enter price: "))

quantity1 = int(input("Enter quantity: "))

sum1 = price1 * quantity1


product2 = input("Enter product: ")

price2 = int(input("Enter price: "))

quantity2 = int(input("Enter quantity: "))

sum2 = price2 * quantity2


product3 = input("Enter product: ")

price3 = int(input("Enter price: "))

quantity3 = int(input("Enter quantity: "))

sum3 = price3 * quantity3


discount_input = input("Enter discount (%): ")

discount_percent = float(discount_input.replace("%", ""))


subtotal = sum1 + sum2 + sum3


discount_amount = subtotal * (discount_percent / 100)


total = subtotal - discount_amount



print("       JAZEL STORE ")

print("==========================")

print("name:", name)

print("contact number:", contact)

print("address:", address)


print("---------------------------")

print("product:", product1)

print("price:", price1)

print("quantity:", quantity1)

print("sum:", sum1)


print("---------------------------")

print("product:", product2)

print("price:", price2)

print("quantity:", quantity2)

print("sum:", sum2)


print("---------------------------")

print("product:", product3)

print("price:", price3)

print("quantity:", quantity3)

print("sum:", sum3)


print("----------------------------")

print("subtotal:", subtotal)

print("discount:", discount_percent, "%")

print("discount amount:", discount_amount)

print("total:", total)

print("----------------------------")

print("   THANK YOU FOR SHOPPING")
