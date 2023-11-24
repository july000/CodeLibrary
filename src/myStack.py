class myStack:
    def __init__(self):
        self.elements = []
        self._size = 0

    def push(self, val):
        self.elements.append(val)
        self._size += 1

    def pop(self):
        if not self.is_empty():
            val = self.elements.pop()
            self._size -= 1
            return val
        else:
            return None

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        return self.elements[-1]
        
    def clear(self):
        self.elements = []
        self._size = 0

my_stack = myStack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.size())
print(my_stack.top())
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.size())

