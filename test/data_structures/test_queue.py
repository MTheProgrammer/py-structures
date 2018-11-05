from unittest import TestCase
from data_structures.Queue import Queue


class TestStack(TestCase):
    def test_is_empty(self):
        q = Queue()
        self.assertEqual(q.is_empty(), True)
        q = Queue([1])
        self.assertEqual(q.is_empty(), False)

    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(42)
        q.enqueue(37)
        q.enqueue('foo')
        self.assertEqual(q.dequeue(), 42)
        self.assertEqual(q.dequeue(), 37)
        self.assertEqual(q.dequeue(), 'foo')

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q = Queue([42, 37])
        self.assertEqual(q.size(), 2)
