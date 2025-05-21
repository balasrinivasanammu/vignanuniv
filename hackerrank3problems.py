def lonelyinteger(a):
    result = 0
    for num in a:
        result ^= num
    return result

def camelcase(s):
    count = 1  
    for char in s:
        if char.isupper():
            count += 1
    return count

#or

def camelcase(s):
    count = 1  
    for char in s:
        if 'A' <= char <= 'Z':  
            count += 1
    return count

def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  
        else:
            stack.append(char)
    
    result = ''.join(stack)
    return result if result else "Empty String"


