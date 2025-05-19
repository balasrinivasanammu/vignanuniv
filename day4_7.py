def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def are_both_sorted(lst1, lst2):
    return is_sorted(lst1) and is_sorted(lst2)

a = [1, 2, 3, 4]
b = [5, 6, 7]

print(are_both_sorted(a, b))  # Output: True

c = [1, 3, 2]
d = [4, 5, 6]

print(are_both_sorted(c, d))  # Output: False
