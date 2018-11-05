
class Stack:

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            raise Exception('Unable to peek empty Stack')

        return self.items[self.size()-1]

    def size(self):
        return len(self.items)
