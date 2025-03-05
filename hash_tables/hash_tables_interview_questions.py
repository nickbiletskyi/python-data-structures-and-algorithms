

def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)

    return duplicates


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))

"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""


def first_non_repeating_char(string):
    l_count = {}
    for l in string:
        l_count[l] = l_count.get(l, 0) + 1

    for key, value in l_count.items():
        if value == 1:
            return key


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""


# def two_sum(nums, target):
#     diff = {}
#     for n in nums:
#         if target > n:
#             diff[n] = target - n
#
#     anagrams = []
#     for index, num in enumerate(nums):
#         if num in list(diff.values())[index+1:]:
#             anagrams.append(index)
#     return anagrams



def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []



print('-' * 100)
print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""

print('-' * 100)

def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num

        if (current_sum - target) in sum_index:
            return [sum_index[current_sum - target] + 1, i]

        sum_index[current_sum] = i

    return []



nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

print('-' * 100)

def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True





print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False


def find_pairs(arr1, arr2, target):
    set_arr1 = set(arr1)

    pairs = []
    for item in arr2:
        diff = target - item
        if diff in set_arr1:
            pairs.append((diff, item))

    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)

"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""