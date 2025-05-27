import re
def is_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
    return re.match(pattern, ip) is not None

# Example
print(is_valid_ip("0.198.99.252"))   # True
print(is_valid_ip("256.100.1.1"))   # False
