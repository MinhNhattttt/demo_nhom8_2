import nltk
from nltk.chat.util import Chat, reflections

# Định nghĩa các cặp câu hỏi và trả lời
chat = [
    (r"hi|hello|hey", ["Hello!", "Hi there!"]),
    (r"how are you?", ["I'm good, how are you?"]),
    (r"fine|good", ["Ohhh, that's good"]),
    (r"what is your name?", ["My name is Chatbot."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!"]),
]

# Tạo chatbot
chatbot = Chat(chat, reflections)

# Chạy chatbot
print("Hi! I'm a chatbot. Type 'bye' to exit.")
chatbot.converse()
