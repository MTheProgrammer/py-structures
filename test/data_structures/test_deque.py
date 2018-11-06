from unittest import TestCase
from data_structures.Deque import Deque


class TestDeque(TestCase):

    def test_add_front(self):
        d = Deque()
        d.add_front(42)
        d.add_front(37)
        self.assertEqual(d.remove_front(), 37)
        self.assertEqual(d.remove_front(), 42)

    def test_add_rear(self):
        d = Deque()
        d.add_rear(42)
        d.add_rear(37)
        self.assertEqual(d.remove_rear(), 37)
        self.assertEqual(d.remove_rear(), 42)

    def test_is_empty(self):
        d = Deque()
        self.assertEqual(d.is_empty(), True)
        d = Deque([1])
        self.assertEqual(d.is_empty(), False)

    def test_size(self):
        d = Deque()
        self.assertEqual(d.size(), 0)
        d = Deque([42, 37])
        self.assertEqual(d.size(), 2)


