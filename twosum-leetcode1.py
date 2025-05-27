def twoSum(nums, target):
    num = {} 

    for i in range(len(nums)):
        flag = nums[i]
        reminder = target - flag
        #print(num_map)
        if reminder in num:
           # print(i,[num[flag], i])
           return [num[reminder], i]
        num[flag] = i
       # print(num)

    #return []
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))  # Output: [1, 2]
