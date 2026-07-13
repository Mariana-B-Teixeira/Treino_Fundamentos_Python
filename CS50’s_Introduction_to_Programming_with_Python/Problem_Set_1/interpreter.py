calc = input("Digite an arithmetic expression: ")
'''
format: x y z
where:
x is an integer
y is +, -, *, /
z is an integer
'''

num1, signal, num2 = calc.split(" ")
num1 = float(num1)
num2 = float(num2)

if signal == "+":
    print(f"{(num1 + num2):.1f}")

elif signal == "-":
    print(f"{(num1 - num2):.1f}")

elif signal == "*":
    print(f"{(num1 * num2):.1f}")

elif signal == "/":
    print(f"{(num1 / num2):.1f}")
