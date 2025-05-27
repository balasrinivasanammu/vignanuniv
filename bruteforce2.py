def brute_force_crack(target_password, max_length=4):
    characters = 'abcdefghijklmnopqrstuvwxyz'

    def generate(current):
        if len(current) > max_length:
            return
        if current == target_password:
            print(f"\nPassword found: {current}")
            return True
        print(f"Trying: {current}")
        for ch in characters:
            if generate(current + ch):
                return True
        return False

    generate('')

# Example usage
target = "dog"
brute_force_crack(target)
