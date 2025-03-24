import unittest


class Console_friend:
    # Метод, возвращающий ответ на сообщение
    # Параметр msg - текст сообщения пользователя
    # return - ответ консольного друга
    def answer_on_message(self,msg): #todo
        if msg == "Скажи, как у тебя дела?":
            return "Хорошо!"
        return "Ответ на сообщение"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        friend_obj = Console_friend()
        self.assertIsNotNone(friend_obj, "Объект класса не создан!")
    def test_answer_message(self):
        friend_obj = Console_friend()
        self.assertEqual("Хорошо!",friend_obj.answer_on_message("Скажи, как у тебя дела?"),"Совпадение")
    def test_fileread(self):
        friend_obj = Console_friend()
        self.assertEqual("Записано в файл",friend_obj.fileread("Text.txt"))




