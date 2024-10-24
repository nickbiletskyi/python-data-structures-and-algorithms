class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedLists:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop_node(self):
        if self.length == 0:
            return
        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):  # or range(self.length, index, -1)
                temp = temp.prev

        return temp

    def set_value(self, index, value):

        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_node(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_node()

        temp = self.get(index)
        if temp:
            before = temp.prev
            after = temp.next
            before.next = after
            after.prev = before
            temp.prev = None
            temp.next = None
            self.length -= 1
        return temp

    def swap_first_and_last(self):
        if self.length > 1:
            first = self.head.value
            self.head.value = self.tail.value
            self.tail.value = first
            return True




















my_d_list = DoublyLinkedLists(1)
my_d_list.append_node(2)
my_d_list.append_node(3)
my_d_list.pop_node()
my_d_list.prepend(0)
my_d_list.prepend(22)
my_d_list.pop_first()
my_d_list.prepend(25)
my_d_list.prepend(24)
my_d_list.set_value(2, 100)
my_d_list.insert(1, 101)
my_d_list = DoublyLinkedLists(1)
# my_d_list.remove(0)



if __name__ == '__main__':
    my_d_list.print_list()
    print('-------')
    print(my_d_list.length, ' len')
    print('-------')
