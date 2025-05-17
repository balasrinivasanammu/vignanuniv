
num = int(input("Enter a number: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


prev_num = num - 1
while prev_num > 1:
    if is_prime(prev_num):
        print("Previous prime number is:", prev_num)
