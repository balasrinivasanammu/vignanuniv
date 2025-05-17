'''a = float(input("Enter first: "))
b = float(input("Enter second: "))
op = input("Enter op (+, -, *, /): ")

if op == '+':
    print("Ans:", a + b)
elif op == '-':
    print("Ans:", a - b)
elif op == '*':
    print("Ans:", a * b)
elif op == '/':
    print("Ans:", a / b)
else:
    print("Invalid op")
    
'''    
a = float(input("Enter first: "))
b = float(input("Enter second: "))
op = input("Enter operation (+, -, *, /): ")

ans = (a + b if op == '+' else
          a - b if op == '-' else
          a * b if op == '*' else
          a / b if op == '/' and b != 0 else
          "Invalid operation or division by zero")

print("Answer:", ans)


