from unittest import TestCase
from data_structures.Stack import Stack


class TestStack(TestCase):
    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push('foo')
        self.assertEqual(s.pop(), 'foo')
        self.assertEqual(s.pop(), 1)

    def test_is_empty(self):
        s = Stack()
        self.assertEqual(s.is_empty(), True)
        s.push(42)
        self.assertEqual(s.is_empty(), False)
        s.pop()
        self.assertEqual(s.is_empty(), True)

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(42)
        self.assertEqual(s.size(), 1)
        s.push(64)
        self.assertEqual(s.size(), 2)

    def test_peek(self):
        s = Stack([42, 37])
        self.assertEqual(s.peek(), 37)

    def test_peekThrows(self):
        s = Stack()
        self.assertRaises(Exception, s.peek)

