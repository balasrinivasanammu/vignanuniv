#1. Constant Time – O(1)

def get_first_element(arr):
    return arr[0]

print(get_first_element([10, 20, 30]))

#2. Linear Time – O(n)
def print_elements(arr):
    for elem in arr:
        print(elem)

print_elements([1, 2, 3, 4, 5])

#3. Quadratic Time – O(n²)
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

print_pairs([1, 2, 3])


#4. Cubic Time – O(n³)
def print_triplets(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)

print_triplets([1, 2])


#5. Exponential Time – O(2ⁿ) (Fibonacci)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))


#6. O(n log n) Using Built-in Sort
arr = [7, 3, 1, 4, 9]
sorted_arr = sorted(arr)
print(sorted_arr)


