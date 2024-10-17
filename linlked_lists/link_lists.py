class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        new_node = Node(value)
        if self.length >= 1:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop_node(self):
        if self.length == 0:
            return

        if self.length == 1:
            pop_node = self.head.value
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next

            pop_node = temp.next.value
            temp.next = None
            self.tail = temp

        self.length -= 1
        return pop_node

    def pop_node_pre(self):
        if self.length == 0:
            return
        if self.length == 1:
            pop_node = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return pop_node
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next  # 1 2 3

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp.value

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return

        pop_item = self.head

        if self.length == 1:
            self.head = None
            self.tail = None

        self.head = pop_item.next
        self.length -= 1
        return pop_item.value

    def get(self, index):
        if self.length == 0:
            return

        if index >= self.length or index < 0:
            return

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value





my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
my_linked_list.append_node(5)
my_linked_list.append_node(6)
my_linked_list.append_node(7)
my_linked_list.print_linked_list()
# print(my_linked_list.pop_node())
print(my_linked_list.pop_node_pre())
print('------')
my_linked_list.print_linked_list()
print('------')
my_linked_list.prepend(1)
my_linked_list.print_linked_list()
print('------')
my_linked_list.pop_first()
my_linked_list.print_linked_list()
print(my_linked_list.get(2))


