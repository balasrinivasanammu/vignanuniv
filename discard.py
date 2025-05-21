my_set = {1, 2, 3, 4, 5}

print("Original set:", my_set)

# Discard an existing element
my_set.discard(3)
print("After discarding 3:", my_set)

# Discard a non-existing element (no error)
my_set.discard(10)
print("After attempting to discard 10:", my_set)
