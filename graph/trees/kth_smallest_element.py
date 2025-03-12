class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def kth_smallest(self, k):
        current_value = [0]
        k_counter = [k]


        
        def traverse_in_order(current_node):
            if current_node.left:
                traverse_in_order(current_node.left)
            if k_counter[0] >= 0:
                k_counter[0] -= 1
            else:
                return
            if k_counter[0] == 0:
                current_value[0] = current_node.value
                return
            if current_node.right:
                traverse_in_order(current_node.right)

        traverse_in_order(self.root)

        return current_value[0]










bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)


print('asdasd ads asd asd as das dads ')
print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7

"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """