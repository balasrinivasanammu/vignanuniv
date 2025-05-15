#1. Decimal to Binary Conversion
def decimal_to_binary(n):
    return bin(n)[2:]

print(decimal_to_binary(10))  # Output: 1010


#2. Binary to Decimal Conversion
def binary_to_decimal(b):
    return int(b, 2)

print(binary_to_decimal('1010'))  # Output: 10

#3. Add Two Binary Numbers
def add_binary(a, b):
    sum_decimal = int(a, 2) + int(b, 2)
    return bin(sum_decimal)[2:]

print(add_binary('1010', '0011'))  # Output: 1101

#4. Subtract Two Binary Numbers
def subtract_binary(a, b):
    diff = int(a, 2) - int(b, 2)
    return bin(diff)[2:] if diff >= 0 else '-' + bin(-diff)[2:]

print(subtract_binary('1010', '0011'))  # Output: 0111

#6. Binary to Octal Conversion
def binary_to_octal(b):
    return oct(int(b, 2))[2:]

print(binary_to_octal('1010'))  # Output: 12

#7. Binary to Hexadecimal Conversion
def binary_to_hex(b):
    return hex(int(b, 2))[2:].upper()

print(binary_to_hex('1010'))  # Output: A

#9. Count Number of 1’s in a Binary Number
def count_ones(b):
    return b.count('1')

print(count_ones('101011'))  # Output: 4

#10. Check if a Number is a Power of Two (Binary Form)
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(8))   # Output: True
print(is_power_of_two(10))  # Output: False
