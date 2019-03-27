import os
import sys
import unittest

PROJECT_ROOT = os.path.join(os.path.join(os.path.dirname(__file__), '..'), 'src')
sys.path.insert(0, os.path.abspath(PROJECT_ROOT))

from classes import ParentClassOne, ChildClass


class TestParentClassOne(unittest.TestCase):

    def setUp(self):
        self.object = ParentClassOne()

    def test_count(self):
        self.assertTrue(self.object.count >= 0)
        self.assertIsInstance(self.object.count, int)

    def test_instance_variable(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
