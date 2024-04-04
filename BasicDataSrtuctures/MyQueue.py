class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

class MyQueue(object):

    def __init__(self):
        # stack to store elements
        self.stack1 = Stack()
        # temporary stack for reversing elements
        self.stack2 = Stack()

    def push(self, x):
        # loop to transfer all elements from stack1 to stack2
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        # push the new element to stack1
        self.stack1.push(x)
        
        # loop to transfer all elements back from stack2 to stack1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def peek(self):
        return self.stack1.top()

    def empty(self):
        return self.stack1.is_empty()