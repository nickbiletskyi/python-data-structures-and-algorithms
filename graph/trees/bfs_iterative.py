from collections import deque
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

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        queue = deque([self.root])
        results = []
        while queue:
            current_node = queue[0]
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            results.append(queue.popleft().value)

        return results

    def BFS_r(self):
        return self.__traverse_BFS_r(queue=deque([self.root]), results=[])

    def __traverse_BFS_r(self, queue, results):
        if len(queue) == 0:
            return results
        current_node = queue[0]
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        results.append(queue.popleft().value)  # we use deque popleft instead of queue.pop(0) because pop(0) will be o(n) and queue.popleft() is o(1)
        return self.__traverse_BFS_r(queue, results)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())
print(my_tree.BFS_r())

"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """









