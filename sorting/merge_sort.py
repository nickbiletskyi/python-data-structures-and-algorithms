

def merge(list1, list2):
    """
    takes two sorted list and merge them in a sorted list
    """
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    combined.extend(list1[i:])
    combined.extend(list2[j:])

    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    
    mid_index = int(len(my_list)/2)
    
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


original_list = [3,1,5,2]

print(merge_sort(original_list))