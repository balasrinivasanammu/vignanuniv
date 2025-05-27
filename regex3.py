import re
def is_valid_phone(phone):
    pattern = r'^\+?\d{10,13}$'  # Accepts optional + and 10-13 digits
    return re.match(pattern, phone) is not None

# Example
print(is_valid_phone("9876543210"))       # True
print(is_valid_phone("+919876546767"))    # True
print(is_valid_phone("98765"))            # False
