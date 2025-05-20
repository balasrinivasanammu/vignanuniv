#leetcode 189- Rotate Array
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))

print(3%7)