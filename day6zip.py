The zip() function in Python is used to combine multiple iterables
(like lists or tuples) element-wise into tuples.

#Syntax:
#zip(iterable1, iterable2, ...)

#1. Combine Two Lists
names = ['Chennai', 'Baby', 'Goodday']
scores = [85, 90, 95]

zipped = zip(names, scores)
print(list(zipped))
# Output: [('Chennai', 85), ('Baby', 90), ('Goodday', 95)]


#2. Iterate with zip()
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# 3. Different Lengths — stops at the shortest iterable
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))
# Output: [(1, 'a'), (2, 'b')]

# 4.. Unzipping Using *
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters)  # Output: ('a', 'b', 'c')
print(numbers)  # Output: (1, 2, 3)

# 5. Use with dict() to build dictionaries
keys = ['name', 'age']
values = ['Chennai', 25]
d = dict(zip(keys, values))
print(d)  # Output: {'name': 'Chennai', 'age': 25}

# 6. Use with zip(*matrix) to transpose a matrix
matrix = [[1, 2, 3],
          [4, 5, 6]]

transposed = list(zip(*matrix))
print(transposed)
# Output: [(1, 4), (2, 5), (3, 6)]



