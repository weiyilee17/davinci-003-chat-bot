from os import getenv

import openai


class ChatBot:
    def __init__(self):
        openai.api_key = getenv('CHAT_BOT_API_KEY')

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=3000,
            # Low temperatures provide more accurate answers, but the answers are less diverse
            temperature=0.5
        ).choices[0].text

        return response


if __name__ == '__main__':
    chat_bot = ChatBot()
    print(chat_bot.get_response('Hi, how are you?'))
