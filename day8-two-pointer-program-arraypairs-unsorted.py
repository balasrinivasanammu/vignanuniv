def pair_sum_unsorted(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False

print(pair_sum_unsorted([10, 15, 3, 7], 17))  # True
