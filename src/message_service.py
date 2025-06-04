class MessageService:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def clear_messages(self):
        self.messages = []
        
    def update_message(self, index: int, new_message: dict):
        if 0 <= index < len(self.messages):
            self.messages[index] = new_message
            return True
        return False