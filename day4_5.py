def most_frequent_number(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_count = 0
    most_frequent = None
    for num in freq:
        if freq[num] > max_count:
            max_count = freq[num]
            most_frequent = num
            
    return most_frequent

lst = [1, 3, 1, 3, 2, 1]
print(most_frequent_number(lst))  # Output: 1
