#unpack 3 variables
a, b, c = map(int, input("Enter three numbers separated by space: ").split())
print("a =", a)
print("b =", b)
print("c =", c)



#Get string input and unpack it
first_name, last_name = input("Enter your first and last name: ").split()
print("First Name:", first_name)
print("Last Name:", last_name)

#Store multiple numbers in a list (without variable unpacking)
numbers = list(map(int, input("Enter numbers: ").split()))
print("List of numbers:", numbers)


