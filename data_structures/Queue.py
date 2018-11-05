
class Queue:

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
