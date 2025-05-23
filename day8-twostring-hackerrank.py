def twoStrings(s1, s2):
    
    set1 = set(s1)# Convert strings to sets of characters
    set2 = set(s2)
    #print(set1)
    
    if set1.intersection(set2):
        return "YES"
    else:
        return "NO"
    
print(twoStrings("hello", "world"))  # YES
print(twoStrings("hi", "world"))     # NO

