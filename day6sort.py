arr = [5, 2, 9, 1]
arr.sort()
print(arr)  # Output: [1, 2, 5, 9]

arr = [5, 2, 9, 1]
new_arr = sorted(arr)
print(arr)      # Original remains: [5, 2, 9, 1]
print(new_arr)  # Output: [1, 2, 5, 9]


#-----------------------

words = ['banana', 'apple', 'kiwi']
print(sorted(words, key=len))  # Output: ['kiwi', 'apple', 'banana']

arr = [10,30,20]
print(sorted(arr, reverse=True))  # Output: [3, 2, 1]
