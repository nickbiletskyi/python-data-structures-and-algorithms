
hey = [4,2,6,5,1,3]

def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        swapped = False
        for index in range(i):
            if my_list[index] > my_list[index+1]:
                temp = my_list[index]
                my_list[index] = my_list[index+1]
                my_list[index+1] = temp
                swapped = True
        if not swapped:
            return my_list
    return my_list


print(bubble_sort(hey))

        