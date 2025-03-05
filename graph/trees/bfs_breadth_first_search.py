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

    def bfs(self):
        queue = [self.root]
        results = []

        while queue:
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            results.append(current_node.value)

        return results

    def bfs_r(self, queue, results):
        if len(queue) == 0:
            return results

        current_node = queue.pop(0)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        results.append(current_node.value)
        return self.bfs_r(queue, results)










my_bst = BinarySearchTree()
my_bst.insert(47)
my_bst.insert(21)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(27)
my_bst.insert(52)
my_bst.insert(82)
# hey = id(my_bst)
# print(my_bst.root.value)
# print(my_bst.root.left.value)
# print(my_bst.root.right.value)
# print(my_bst.contains(1))

print(my_bst.bfs())
print(my_bst.bfs_r(queue=[my_bst.root], results=[]))
