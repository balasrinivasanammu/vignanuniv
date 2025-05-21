#1.anagram

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # Output: True



#2. Find the Longest Word in a Sentence
#max(iterable, key=None, default=None)

empty_list = []
print(max(empty_list, default="No data"))  # Output: 'No data'


names = ["chennai", "baby", "goodday"]
print(max(names, key=len))  # Output: 'goodday'

def longest_word(sentence):
    words = sentence.split()
    return max(words,key=len)

print(longest_word("Python is awesome"))  # Output: 'awesome'


#or
'''
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
'''
