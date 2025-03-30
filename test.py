def walk_r(steps):
    if steps == 5:
        return steps
    return walk_r(steps + 1) + 1


print(walk_r(1))
anag = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        set_anagrams = set()
        for item in strs:
            sorted_str = ''.join(sorted(item))
            if sorted_str not in set_anagrams: set_anagrams.add(sorted_str)
        
        hash_map_anagrams = {}
        for item in strs:
             sorted_item = ''.join(sorted(item))
             if sorted_item in hash_map_anagrams: hash_map_anagrams[sorted_item].append(item)
             else: hash_map_anagrams[sorted_item] = [item]
                  
        
        list_of_grouped_anagrams = []
        for value in hash_map_anagrams.values():
             list_of_grouped_anagrams.append(value)
        return list_of_grouped_anagrams


print(groupAnagrams(anag))



class Hello:
     def __hash__(self):
          return 1
     

print(Hello().__hash__())


hey = {Hello(): 1}

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print(f"Current count: {count}")
    return increment
counter1 = counter()
counter1()  # "Current count: 1"
counter1()  # "Current count: 2"
print(counter1.__closure__)