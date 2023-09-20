class Stack:

    def __init__(self):
        self.lst = []

    def is_empty(self):
        return len(self.lst) == 0

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if not self.is_empty():
            return self.lst.pop()

    def peek(self):
        if not self.is_empty():
            return self.lst[-1]

    def size(self):
        return len(self.lst)