#Calculadora simples feita em Python.

print("Write your numbers and resolve your math problems: ")

#Make the program read the numbers used and the operator.
num_one = float(input("Enter a number: "))
op = input("Enter operator: ")
num_two = float(input("Enter another number: "))

#sum operator:
if op == "+":
    print(num_one + num_two)
#subtraction operator:
elif op == "-":
    print(num_one - num_two)
#multiplication operator:
elif op == "*":
    print(num_one * num_two)
#Division operator:
elif op == "/":
    print(num_one / num_two)
#If happen any error:
else:
    print("please run the program again! Something gone wrong")

print("Thank you \nfor using \nmy project!")