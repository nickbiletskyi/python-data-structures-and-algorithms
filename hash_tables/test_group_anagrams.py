def group_anagrams(anagrams_list):
    set_anagrams = set([''.join(sorted(item)) for item in anagrams_list])
    grouped = {key: [] for key in set_anagrams}

    for item in anagrams_list:
        sorted_item = ''.join(sorted(item))

        grouped[sorted_item].append(item)

    new_list = []

    for key, value in grouped.items():
        if value:
            new_list.append(value)

    return new_list


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]
"""