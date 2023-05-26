from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def __str__(self):
        string = ""
        for x in self.stack:
            string+= x + ", "
        return string[:-2]

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) ==  0
    
    def size(self):
        return len(self.stack)



    