#1. Create a Matrix (2D Array)
rows, cols = 3, 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)
# Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''
#2. Input Matrix from User
rows = 2
cols = 2
matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} values: ").split()))
    matrix.append(row)

print("Matrix:", matrix)'''

#3. Print Matrix in Row-wise Format
matrix = [[1, 2], [3, 4]]
for row in matrix:
    print(*row)

#4. Transpose of a Matrix
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
# Output: [[1, 4], [2, 5], [3, 6]]

#5. Add Two Matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(result)
# Output: [[6, 8], [10, 12]]

#6. Diagonal Elements (Main & Secondary)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

main_diag = [matrix[i][i] for i in range(len(matrix))]
sec_diag = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]

print("Main:", main_diag)       # Output: [1, 5, 9]
print("Secondary:", sec_diag)   # Output: [3, 5, 7]

#  7. Sum of Each Row and Column
matrix = [[1, 2], [3, 4]]
row_sums = [sum(row) for row in matrix]
col_sums = [sum(col) for col in zip(*matrix)]

print("Row Sums:", row_sums)  # Output: [3, 7]
print("Col Sums:", col_sums)  # Output: [4, 6]
