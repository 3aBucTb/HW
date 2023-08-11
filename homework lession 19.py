class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        if self.url is not None and self.chat_id is not None:
            print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")
        else:
            print("URL and chat ID must be set to send messages.")