class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        elif value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True

        return self.__r_insert(self.root, value)


my_bst = BinarySearchTree()
my_bst.r_insert(2)
my_bst.r_insert(1)
my_bst.r_insert(3)
print(my_bst.r_contains(4))
print(my_bst.r_contains(3))

