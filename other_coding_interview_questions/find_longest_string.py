"""
List: Find Longest String ( ** Interview Question)
Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.

Example:

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest) 
"""

def find_longest_string(string_list):
    longest_str = ''

    for item in string_list:
        if len(item) > len(longest_str):
            longest_str = item
    return longest_str

string_list = ['apple', 'banana', 'kiwi', 'pear']
print(find_longest_string(string_list))
