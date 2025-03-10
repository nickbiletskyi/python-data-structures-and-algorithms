class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first

        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp








my_queue = Queue(1)
my_queue.enqueue(2)
# print(my_queue.first.value)
# my_queue.dequeue()


if __name__ == '__main__':
    my_queue.print_queue()
    print('-------')
    print(my_queue.length, ' len')
    print('-------')

