import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertIsNotNone(self, "Объекта класса не существует")  # add assertion here



