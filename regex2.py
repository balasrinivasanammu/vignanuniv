import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# Example
print(is_valid_email("example@test.com"))  # True
print(is_valid_email("example@test"))      # False
