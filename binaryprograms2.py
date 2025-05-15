#1. Check if a Number is Even or Odd Using Bitwise AND
def is_even(n):
    return (n & 1) == 0

print(is_even(4))  # True
print(is_even(7))  # False

#2. Check if a Number is a Power of Two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(8))  # True
print(is_power_of_two(10)) # False


#3. Get the ith Bit
def get_ith_bit(n, i):
    return (n >> i) & 1

print(get_ith_bit(13, 2))  # Output: 1 (13 is 1101 in binary)


#
#4. Toggle the ith Bit

def toggle_ith_bit(n, i):
    return n ^ (1 << i)

print(toggle_ith_bit(13, 2))  # Output: 9

