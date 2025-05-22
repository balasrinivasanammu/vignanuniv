def minimumNumber(n, password):
    has_digit = 0
    has_lower = 0
    has_upper = 0
    has_special = 0

    special_characters = "!@#$%^&*()-+"

    for c in password:
        ascii_val = ord(c)

        
        if ascii_val >= 48 and ascii_val <= 57:
            has_digit = 1
      
        elif ascii_val >= 97 and ascii_val <= 122:
            has_lower = 1
        
        elif ascii_val >= 65 and ascii_val <= 90:
            has_upper = 1
      
        elif c in special_characters:
            has_special = 1

    missing_types = 4 - (has_digit + has_lower + has_upper + has_special)
    return max(missing_types, 6 - n)


n = 11
# test cases - doesnot checks the length of input string
password = "#Hackerrank"
print(minimumNumber(n, password))  # Output: 1
