x = float(input("enter 1st number: "))
y = float(input("enter 2nd number: "))

op = input("enter a operator (+, -, *, /): ")

if op == "+":
    print(x + y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("wrong input given..")
