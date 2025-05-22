
#Note: Code not optimized
# 1 test case failed due to count of freq's
# 2nd test case failed due to alpha numeric
# time complexity high
# 
def decode_string(s):
    i = 0
    output = ''   
    while True:        
        try:
            s[i]
           # print(s[i])
        except:
            break
        ch = s[i] # character ----> a
        digit_char = s[i + 1] # digits of neighbour character like a1     
        digit = ord(digit_char) - ord('0') # convert numeric ascii value 49-48
        count = 0
        while count < digit: # 
            output += ch
            count += 1
        i += 2
    print(output)
decode_string('a1b2c2d4')  # Output: abbcc




