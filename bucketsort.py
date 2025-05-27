def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    # Step 2: Put array elements into different buckets
    for value in arr:
        index = int(value * num_buckets)  # index in range [0, num_buckets-1]
        if index != num_buckets:
            buckets[index].append(value)
        else:
            buckets[num_buckets - 1].append(value)  # handle edge case where value == 1

    # Step 3: Sort individual buckets
    for i in range(num_buckets):
        buckets[i].sort()

    # Step 4: Concatenate all buckets into a single array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Example usage
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print("Original:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted:", sorted_arr)
