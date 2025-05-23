my_set = {1, 2, 3}
updates = [3, 4, 5]
my_set.update(updates)
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_dict = {'a': 1, 'b': 2}
updates = {'b': 3, 'c': 4, 'b':5}
my_dict.update(updates)
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}










'''

Dictionaries
The update() method merges a dictionary with another dictionary
or an iterable of key-value pairs. It modifies the original dictionary in place,
adding new keys or updating the values of existing keys


Sets
The update() method adds elements from another set or any iterable to a set.
It also modifies the original set in place, and duplicate elements are automatically removed.
'''