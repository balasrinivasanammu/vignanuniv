def has_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left],arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False

print(*has_pair_with_sum([1,2,3,4,5,6], 9))  # True (3+6)


















