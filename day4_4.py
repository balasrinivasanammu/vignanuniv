def is_sorted(lst):
    ascending = True
    descending = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            ascending = False
        if lst[i] < lst[i + 1]:
            descending = False
    return ascending or descending


print(is_sorted([1, 2, 3, 4]))     # True (ascending)
print(is_sorted([4, 3, 2, 1]))     # True (descending)
print(is_sorted([1, 3, 2, 4]))     # False
