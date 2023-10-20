import unittest
import datetime
from .context import split

class SplitTest(unittest.TestCase):
    def test_format_time(self):
        simple_time = datetime.timedelta(0,10)
        self.assertEqual(split.format_time(simple_time), "00:00:10.0")
