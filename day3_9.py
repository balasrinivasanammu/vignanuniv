num = int(input("Enter a number: "))
sum_of_powers = sum(int(digit)**len(str(num)) for digit in str(num))
if sum_of_powers == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
