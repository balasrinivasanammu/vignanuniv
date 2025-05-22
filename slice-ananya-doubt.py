def super_reduced_string(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i+2:]  
            print(s[:i],s[i+2:])
            i = max(i - 1, 0)    # clue for step back to check pairs
        else:
            i += 1

    return s if s else "Empty String"

print(super_reduced_string("baalaji"))  # Output: "blaji"
