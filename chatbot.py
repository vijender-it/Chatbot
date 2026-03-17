# Sample Chatbot Implementation

class Chatbot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello! My name is {self.name}. How can I assist you today?"

    def respond(self, user_input):
        return f"You said: {user_input}. I'm still learning!"

if __name__ == '__main__':
    bot = Chatbot('Assistant')
    print(bot.greet())
    user_input = input("Say something: ")
    print(bot.respond(user_input))