
def anagrams(str1, str2):

    length1 = 0
    for ch in str1:
        length1 += 1
    length2 = 0
    for ch in str2:
        length2 += 1
    if length1 != length2:
        return False

    s1 = ''
    for ch in str1:
        if 'A' <= ch <= 'Z':
            s1 += chr(ord(ch) + 32)
        else:
            s1 += ch

    s2 = ''
    for ch in str2:
        if 'A' <= ch <= 'Z':
            s2 += chr(ord(ch) + 32)
        else:
            s2 += ch

    count1 = [0] * 26
    count2 = [0] * 26

    for ch in s1:
        if 'a' <= ch <= 'z':
            index = ord(ch) - ord('a')
            count1[index] += 1

    for ch in s2:
        if 'a' <= ch <= 'z':
            index = ord(ch) - ord('a')
            count2[index] += 1

    
    for i in range(26):
        if count1[i] != count2[i]:
            return False

    return True


str1 = "Listen"
str2 = "Silent"

if anagrams(str1, str2):
    print("Yes, anagrams.")
else:
    print("Not anagrams.")
