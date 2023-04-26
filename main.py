from sys import exit, argv
from threading import Thread

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication

from backend import ChatBot


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)
        self.setWindowTitle('ChatBot using text-davinci-003 model')

        self.chat_bot = ChatBot()
        self.chat_area_text_edit = QTextEdit(self)
        self.chat_area_text_edit.setGeometry(10, 10, 600, 480)
        self.chat_area_text_edit.setReadOnly(True)

        self.user_input_line_edit = QLineEdit(self)
        self.user_input_line_edit.setGeometry(10, 500, 600, 40)
        # onPressEnter
        self.user_input_line_edit.returnPressed.connect(self.send_message)

        self.submit_push_button = QPushButton('Send', self)
        self.submit_push_button.setGeometry(620, 500, 100, 40)
        self.submit_push_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.user_input_line_edit.text().strip()
        self.chat_area_text_edit.append(
            f'<p style="color: white; background-color: #343541; font-size: 24px;"> Me: {user_input}</p>')

        self.user_input_line_edit.clear()
        self.submit_push_button.setDisabled(True)

        chat_bot_response_thread = Thread(target=self.get_chat_bot_response, args=(user_input,))
        chat_bot_response_thread.start()

    def get_chat_bot_response(self, user_input_arg):
        chat_bot_response = self.chat_bot.get_response(user_input_arg)
        self.chat_area_text_edit.append(
            f'<p style="color: white; background-color: #444645; font-size: 24px;"> ChatBot: {chat_bot_response}</p>'
        )
        self.submit_push_button.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(argv)
    main_window = ChatBotWindow()
    exit(app.exec())
