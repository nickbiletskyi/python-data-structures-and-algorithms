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

    def dfs_in_order(self):
        return self.traverse_in_order(self.root, [])

    def dfs_pre_order(self):
        return self.traverse_pre_order(self.root, [])

    def dfs_post_order(self):
        return self.traverse_post_order(self.root, [])

    def traverse_in_order(self, current_node, results):
        """left-root-right"""
        if current_node.left:
            self.traverse_in_order(current_node.left, results)  # go all the way down until it's left child
        results.append(current_node.value)  # when there is no more left child append value to the results

        if current_node.right:
            self.traverse_in_order(current_node.right, results)

        return results

    def traverse_pre_order(self, current_node, results):
        """root-left-right"""
        results.append(current_node.value)  # when there is no more left child append value to the results

        if current_node.left:
            self.traverse_pre_order(current_node.left, results)  # go all the way down until it's left child

        if current_node.right:
            self.traverse_pre_order(current_node.right, results)

        return results



    def traverse_post_order(self, current_node, results):
        """left-right-root"""

        if current_node.left:
            self.traverse_post_order(current_node.left, results)  # go all the way down until it's left child

        if current_node.right:
            self.traverse_post_order(current_node.right, results)

        results.append(current_node.value)


        return results

my_bst = BinarySearchTree()
my_bst.insert(9)
my_bst.insert(4)
my_bst.insert(20)
my_bst.insert(1)
my_bst.insert(6)
my_bst.insert(15)
my_bst.insert(170)

"""
               9
        4              20
    1      6       15      170
    
"""
# hey = id(my_bst)
# print(my_bst.root.value)
# print(my_bst.root.left.value)
# print(my_bst.root.right.value)
# print(my_bst.contains(1))

# print(my_bst.bfs())
print(my_bst.bfs_r(queue=[my_bst.root], results=[]))
print(my_bst.dfs_post_order())
print(my_bst.dfs_pre_order())
print(my_bst.dfs_in_order())
