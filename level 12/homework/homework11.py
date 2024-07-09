number1 = int(input("please enter number "))
sign = input("please enter sign ")
number2 = int(input("please enter second number "))

if sign == "x":
    print(number1 * number2)
elif sign == "%":
    print(number1 / number2)
elif sign == "+":
    print(number1 + number2)
else:
    print(number1 - number2)




