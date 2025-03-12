from collections import deque

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
        queue = deque([self.root])
        results = []

        while queue:
            current_node = queue.popleft()
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results
    
    def bfs_r(self):
        queue = deque([self.root])
        return self.traverse_bfs(queue=queue, results=[])



    def traverse_bfs(self, queue, results):
        if not queue:
            return results
        current_node = queue.popleft()
        results.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.traverse_bfs(queue, results)
    
    def invert_tree(self, current_node):
        if not current_node:
            return
        current_node.left, current_node.right = current_node.right, current_node.left

        self.invert_tree(current_node.left)
        self.invert_tree(current_node.right)

        return current_node
        


my_bst = BinarySearchTree()
my_bst.insert(4)
my_bst.insert(2)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(3)
my_bst.insert(6)
my_bst.insert(9)
print(my_bst.bfs_r())
print(my_bst.bfs())
print(my_bst.root.value)
my_bst.invert_tree(my_bst.root)
print(my_bst.bfs())


