def subset_sums(arr):
    sums = {0}
    for num in arr:
        new_sums = set()
        for s in sums:
            new_sums.add(s + num)
        sums.update(new_sums)
    return sums

arr = [1, 2, 3]
print(subset_sums(arr))  # Output: {0, 1, 2, 3, 4, 5, 6}


'''
Example:

Input: [1, 2, 3]

Possible subsets and their sums:

    [] → sum = 0

    [1] → sum = 1

    [2] → sum = 2

    [3] → sum = 3

    [1, 2] → sum = 3

    [1, 3] → sum = 4

    [2, 3] → sum = 5

    [1, 2, 3] → sum = 6

All possible sums: {0, 1, 2, 3, 4, 5, 6}
'''

'''
Step-by-step example with [1, 2, 3]:

    Start: sums = {0}

    Add 1:

        For each sum in {0}, add 1 → 0 + 1 = 1

        New sums: {0, 1}

    Add 2:

        For each sum in {0, 1}, add 2 → 0 + 2 = 2, 1 + 2 = 3

        New sums: {0, 1, 2, 3}

    Add 3:

        For each sum in {0, 1, 2, 3}, add 3 → 0 + 3 = 3, 1 + 3 = 4, 2 + 3 = 5, 3 + 3 = 6

        New sums: {0, 1, 2, 3, 4, 5, 6}
'''