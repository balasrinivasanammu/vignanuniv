# 1. Check if a Number is Even or Odd
n = 7
print("Even" if n & 1 == 0 else "Odd")








# 2. Check if nth Bit is Set
n = 18  # 10010
bit = 4
print("Bit is set" if (n & (1 << bit)) else "Bit is not set")

'''
Notes:
18 → 10010

Bit positions (from right to left):
4   3   2   1   0
1   0   0   1   0
'''

if n & (1 << bit):
    print("Bit is set")
else:
    print("Bit is not set")

# Set nth Bit

n = 18
bit = 1
n |= (1 << bit) # n=n| (1<<bit)
print("After setting bit:", n)

# swap 2 numbers using xor
a = 5
b = 9
a ^= b
b ^= a
a ^= b
print("a:", a, "b:", b)

