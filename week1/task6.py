num1 = float(input("First number:"))
operatoin = input("Operatiomn:")
num2 = float(input("Second number:"))

if operatoin == "+":
    print(num1 + num2)
elif operatoin == "-":
    print(num1 - num2)
elif operatoin == "*":
    print(num1 * num2)
elif operatoin == "/":
    print(num1 / num2)
else:
    print("Error")