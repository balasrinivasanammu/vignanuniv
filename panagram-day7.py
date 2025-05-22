def panagram(sentence):
    
    flag = [0] * 26  

    for ch in sentence:
        
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)

        if 'a' <= ch <= 'z':
            ind = ord(ch) - ord('a')
            flag[ind] = 1

    for i in range(26):
        if flag[i] == 0:
            return False

    return True
    
#inputstring = "The quick brown fox jumps over the lazy dog"
inputstring = "abc defg _ 10@ hijklmnopqrstuvwxyz"

if panagram(inputstring):
    print("It is a pangram.")
else:
    print("Its not a pangram.")

