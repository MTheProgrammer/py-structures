from collections import deque


class Palindrome:
    def __init__(self, text):
        self.text = text

    def execute(self):
        d = deque(self.text)
        while len(d):
            if not d.pop() == d.popleft():
                return False
        return True
