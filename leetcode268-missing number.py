def missingNumber(nums):
    n = len(nums)
    result = n
    for i in range(n):
        result ^= i ^ nums[i]# result=result ^ i ^ nums[i]
    return result

nums = [0]
#nums = [3,0,1]
#nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))

'''
0 0 1 0
0 0 0 0
0 0 1 0 ^
0 0 0 0
0 0 1 0 -> 1 (result)

0 0 1 0
0 0 0 1
0 0 1 1 ^
0 0 0 1
0 0 1 0 -> 2 (result)

'''
'''
n = len(nums)
total_sum = n * (n + 1) // 2
return total_sum - sum(nums)
'''