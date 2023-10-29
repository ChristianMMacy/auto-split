import unittest
from .context import split

class SplitTest(unittest.TestCase):
    def test_youtube(self):
        split.hit_youtube()
