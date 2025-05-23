def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    #print(s1)
    #print(s2)
    left, right = 0, len(s1) - 1
    while left < len(s1):
        if s1[left] != s2[left]:
            return False
        left += 1
    return True

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "bello"))    # False
