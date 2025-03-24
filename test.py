import unittest


class Console_friend:
    pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        friend_obj = Console_friend()
        self.assertIsNotNone(friend_obj, "Объект класса не создан!")  # add assertion here



