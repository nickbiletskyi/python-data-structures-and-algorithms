class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


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
            print(temp)
            if temp.value == value:
                return False
            if temp.value > value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root

        while temp is not None:

            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False


my_bst = BinarySearchTree()
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)
hey = id(my_bst)
print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)
print(my_bst.contains(1))
