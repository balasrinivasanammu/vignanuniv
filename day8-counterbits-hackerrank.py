def counterGame(n):
    turns = 0
    while n != 1:
        if (n & (n - 1)) == 0:
            # n is power of 2
            n >>= 1
        else:
            # subtract the largest power of 2 less than n
            power = 1 << (n.bit_length() - 1)
            n -= power
        turns += 1
    return "Louise" if turns % 2 == 1 else "Richard"

print(counterGame(6))   # Output: Richard
print(counterGame(132)) # Output: Louise
