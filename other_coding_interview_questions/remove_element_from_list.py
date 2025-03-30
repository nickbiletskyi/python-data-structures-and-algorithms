def remove_element(nums, val1):
    """
    Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.
    The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.    
    """
    index = 0
    while index < len(nums):
        if val1 == nums[index]:
            nums.pop(index)
        else:
            index += 1
    return len(nums)

# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1

remove_element(nums1, val1)

print(nums1)