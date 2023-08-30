class Stack:
    def __init__(self):
        self.elements = []
        self._size = 0
        pass
    
    def push(self, val):
        self.elements.append(val)
        self._size += 1

    def pop(self):
        val = self.elements.pop()
        self._size -= 1
        return val

    def size(self):
        return self._size

    def is_empty(self):
        return self._size > 0

    def top(self):
        return self.elements[-1]
        
    def clear(self):
        self.elements = []