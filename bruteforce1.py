def brute_force_pin(target_pin):
    for i in range(0,300):  # 000 to 999
        # Convert i to a 3-digit string manually
        d1 = i // 100
        d2 = (i % 100) // 10
        d3 = i % 10
        attempt = str(d1) + str(d2) + str(d3)
        
        print(f"Trying: {attempt}")
        if attempt == target_pin:
            print(f"\nPIN found: {attempt}")
            return attempt

    print("\nPIN not found.")
    return None

# Example usage
target = "307"
brute_force_pin(target)
