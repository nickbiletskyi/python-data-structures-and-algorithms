
def find_closest_number(nums):

    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num

    return abs(closest) if abs(closest) in nums else closest

nums1 = [-4, -2, 2, 4, 8]
nums = [-2, 2]
print(find_closest_number(nums))
print(find_closest_number(nums1))




def findClosestNumber_hash_map(nums):
    """
    :type nums: List[int]
    :rtype: int
    Final Complexity
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    diff_dict = {}
    for n in nums:
        diff = n - 0
        diff_dict[n] = abs(diff)

    min_ = min(diff_dict.values())

    return diff_dict.get(min_, -min_)


nums1 = [-4, -2, 2, 4, 8]
nums = [-2, 2]
print(findClosestNumber_hash_map(nums))
print(findClosestNumber_hash_map(nums1))
