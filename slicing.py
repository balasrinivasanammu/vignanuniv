nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])      # [1, 2, 3]

print(nums[:3])       # [0, 1, 2]

print(nums[3:])       # [3, 4, 5]

print(nums[:])        # [0, 1, 2, 3, 4, 5]

print(nums[-3:])      # [3, 4, 5]
print(nums[:-2])      # [0, 1, 2, 3]

print(nums[::2])      # [0, 2, 4]

print(nums[::-1])     # [5, 4, 3, 2, 1, 0]

print(nums[-3:])      # [3, 4, 5]

print(nums[:3])       # [0, 1, 2]

nums[1:4] = ['a', 'b']
print(nums)           # [0, 'a', 'b', 4, 5]

nums = [0, 1, 2, 3, 4, 5]
del nums[1:4]
print(nums)           # [0, 4, 5]


copy = nums[:]
print(copy)           # [0, 1, 2, 3, 4, 5]


t = (10, 20, 30, 40, 50)
print(t[1:4])         # (20, 30, 40)


text = "Hello, World!"
print(text[7:12])     # 'World'

print(text[::2])      # 'Hlo ol!'


print(text[1:-1])     # 'ello, World'

#Replace Every Other Element
nums = [0, 1, 2, 3, 4, 5]
nums[::2] = [9, 99,999]
print(nums)           # [9, 1, 9, 3, 9, 5]

#Nested List Slicing
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print([row[1:] for row in matrix])  # [[2,3], [5,6], [8,9]]


nums = [0, 1, 2, 3, 4, 5]
print(2**i for i in range(1,len(nums)) if 2**nums[i]%2==0)

nums =[0, 1, 2, 3, 4, 5]
#print((*nums) *5)# unpacking error bcas of exression syntax

nums =[10,20,30]
print(*nums * 5)
print(2*nums)
#print(5-4*nums)# error as per the bodmas rule and type value error




