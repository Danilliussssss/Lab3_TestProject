import unittest


class Console_friend:
    def answer_on_message(self,msg): #todo
        return "Ответ на сообщение"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        friend_obj = Console_friend()
        self.assertIsNotNone(friend_obj, "Объект класса не создан!")
    def test_answer_message(self):
        friend_obj = Console_friend()
        self.assertEqual("Ответ на сообщение",friend_obj.answer_on_message("Сообщение"),"Совпадение")




