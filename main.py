from test import Console_friend

if __name__ == "__main__":
   while(True):
    msg = input("Введите ваше сообщение: ")
    console_friend = Console_friend()
    answer = console_friend.answer_on_message(msg)
    print(answer)
    fileread_res = console_friend.fileread("Text.txt")
    print(fileread_res)