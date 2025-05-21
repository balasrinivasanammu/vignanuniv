| Operation    | Data Type       | Removes         | Safe if Not Present? | Example               |
| ------------ | --------------- | --------------- | -------------------- | --------------------- |
| `discard(x)` | `set`           | element `x`     | ✅                    | `s.discard(x)`        |
| `remove(x)`  | `set`, `list`   | element `x`     | ❌                    | `s.remove(x)`         |
| `pop()`      | `list`, `deque` | last (or index) | ❌                    | `l.pop()`, `l.pop(0)` |
| `popleft()`  | `deque`         | first element   | ❌                    | `d.popleft()`         |
| `del`        | any             | index/key/slice | ❌                    | `del lst[1]`          |

s = {1, 2, 3}
s.discard(4)  # OK, does nothing
s.remove(4)   # KeyError!


# List
lst = [1, 2, 3, 4]
del lst[2]         # Removes element at index 2 (value 3)
del lst[1:]        # Removes all elements from index 1 onwards

# Dictionary
d = {'a': 1, 'b': 2}
del d['a']         # Removes key 'a'

# Delete a variable
x = 5
del x              # x no longer exists


from collections import deque

l = [1, 2, 3]
l.pop()        # Removes 3
l.pop(0)       # Removes 1 (first element)

d = deque([1, 2, 3])
d.popleft()    # Removes 1 (from left)
