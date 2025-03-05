def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {}

    for index, item in enumerate(nums):
        complement = target - item
        if complement not in nums_dict:
            nums_dict[item] = index
        else:
            return [nums_dict[complement], index]


nums = [2,11,15, 7]
target = 9
print(twoSum(nums, target))

