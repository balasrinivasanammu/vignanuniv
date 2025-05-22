def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # Remove the lowest set bit
        count += 1
    return count

print(count_set_bits(15))  # Output: 4 (1111)


#1. Add Two Numbers Without Using + or -
def add(a, b):
    while b != 0:
        carry = a & b  
        a = a ^ b      
        b = carry << 1 

    return a

print(add(5, 3))  # Output: 8
