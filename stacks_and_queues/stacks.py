class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    def pop_node(self):
        if self.height == 0:
            return
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp










my_stack = Stack(1)
my_stack.push(2)
my_stack.push(2)
my_stack.push(4)
my_stack.pop_node()


if __name__ == '__main__':
    my_stack.print_stack()
    print('-------')
    print(my_stack.height, ' len')
    print('-------')
    print(my_stack.top.value)




