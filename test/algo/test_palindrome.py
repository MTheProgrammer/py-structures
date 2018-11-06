from unittest import TestCase
from unittest_data_provider import data_provider
from algo.Palindrome import Palindrome


class TestPalindrome(TestCase):

    texts = [
        ('abba', True),
        ('toot', True),
        ('radar', True),
        ('binoculars', False),
        ('foo', False),
    ]

    @data_provider
    def test_execute(self, text, expected):
        p = Palindrome(text)
        self.assertEqual(expected, p.execute())

