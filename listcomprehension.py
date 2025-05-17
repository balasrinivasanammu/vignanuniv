#1. Squares of Numbers (1 to 10)
squares = [x**2 for x in range(1, 11)]
print(squares)















#2.Even Numbers (1 to 20)
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

#3. Odd Numbers (1 to 20)
odds = [x for x in range(1, 21) if x % 2 != 0]
print(odds)

#4. Multiples of 3 (1 to 50)
multiples_of_3 = [x for x in range(1, 51) if x % 3 == 0]
print(multiples_of_3)


#5. Convert List of Strings to Uppercase
words = ["balaji", "salem", "yercaud"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# 6. Filtering vowels
letters = ['a', 'b', 'c', 'e', 'i', 'o', 'u']
vowels = [ch for ch in letters if ch in 'aeiou']
print(vowels)

# 7. Flattening a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

# 8. Reverse strings
words = ["python", "list", "comprehension"]
reversed_words = [word[::-1] for word in words]
print(reversed_words)

# 9. Convert to lowercase
mixed = ["Hello", "WORLD", "PyThOn"]
lowercase = [x.lower() for x in mixed]
print(lowercase)

# 10. Create a list of tuples
tuples = [(x, x**2) for x in range(6)]
print(tuples)

# 11. Numbers not divisible by 3 and 5
filtered = [x for x in range(50) if x % 3 != 0 and x % 5 != 0]
print(filtered)

# 12. Lengths of words
lengths = [len(word) for word in ["apple", "banana", "cherry"]]
print(lengths)

# 13. ASCII values
ascii_vals = [ord(ch) for ch in 'hello']
print(ascii_vals)

# 14. Filter positive numbers
nums = [-5, 3, -1, 101, 0, -42]
positives = [x for x in nums if x > 0]
print(positives)

# 15. Nested list comprehension - square matrix
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)

# 16. Digits in a string
sample = "abc123xyz456"
digits = [ch for ch in sample if ch.isdigit()]
print(digits)
