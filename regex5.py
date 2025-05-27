def is_valid_website(url):
    pattern = r'^(https?://)?(www\.)?[\w\-]+\.\w{2,}$'
    return re.match(pattern, url) is not None

# Example
print(is_valid_website("https://example.com"))  # True
print(is_valid_website("example.com"))          # True
print(is_valid_website("example"))              # False
