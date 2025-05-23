def remove_element(nums, val):
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return left

arr = [3,2,2,3]
length = remove_element(arr, 3)
print(arr[:length])  # [2,2]
