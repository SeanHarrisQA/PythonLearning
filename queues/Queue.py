from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def __str__(self):
        string = ''
        for x in self.queue:
            string += x + ', '
        return string[:-2]
    
    def enqueue(self, x):
        self.queue.appendleft(x)

    def dequeue(self):
        return self.queue.pop()
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[-1]