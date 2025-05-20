matrix = []
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

print("The 3x3 matrix is:")
for row in matrix:
    print(row)
