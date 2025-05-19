def move_zeros_to_end(lst):
    result = []
    zero_count = 0
    
    for num in lst:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1
    
    # Append zeros at the end
    result=result+([0] * zero_count)
    return result

def move_zeros_to_start(lst):
    result = []
    zero_count = 0

    for num in lst:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1

    # Prepend zeros at the start
    return [0] * zero_count + result

lst = [0, 1, 0, 3, 12]

print(move_zeros_to_end(lst))   # [1, 3, 12, 0, 0]
print(move_zeros_to_start(lst)) # [0, 0, 1, 3, 12]
