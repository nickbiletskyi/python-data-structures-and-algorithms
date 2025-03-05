class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def sort_stack(stack):
    # Create a new stack to hold the sorted elements
    additional_stack = Stack()

    # While the original stack is not empty
    while not stack.is_empty():
        # Remove the top element from the original stack
        temp = stack.pop()

        # While the additional stack is not empty and
        # the top element is greater than the current element
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            # Move the top element from the additional stack to the original stack
            stack.push(additional_stack.pop())

        # Add the current element to the additional stack
        additional_stack.push(temp)

    # Copy the sorted elements from the additional stack to the original stack
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())

    return stack.stack_list

my_stack = Stack()
my_stack.push(25)
my_stack.push(5)
my_stack.push(7)

print(sort_stack(my_stack))








