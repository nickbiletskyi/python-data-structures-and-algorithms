class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            parent = self._parent(current)
            self._swap(current, parent)
            current = parent

    def remove(self):
        if len(self.heap) == 0:
            return
        if len(self.heap) == 1:
            self.heap.pop()
            return

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # assign it to the top of heap

        self.sink_down(0)

        return max_value


    def sink_down(self, index):

        max_index = index

        while True:
            left_index = self._left_child(max_index)  # determine left child index
            right_index = self._right_child(max_index) # determine right child index

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:  # check that child exists, and if value of max index is less than left child and assign left child to max index
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:  # check that child exists, and if value of max index is less than right and child assign left child to max index
                max_index = right_index

            if max_index != index:  # if max_index was less than left or right child swap them if was not less then return
                self._swap(max_index, index)
                index = max_index  # assign max index to index
            else:
                return


myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)

myheap.insert(100)

print(myheap.heap)

myheap.insert(75)

print(myheap.heap)

"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""

myheap.remove()

print(myheap.heap)

"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 75, 58, 61]

"""
