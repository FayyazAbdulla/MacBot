from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

# Create chatbot
chatbot = ChatBot(
    "MacBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Train chatbot with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)

# Train on built-in corpus
trainer.train("chatterbot.corpus.english")

# Train on your own custom conversations
trainer.train("data/about_me.yml")


# Start conversation loop
print("MacBot is ready to chat! (Type 'exit' to stop)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.get_response(user_input)
    print("MacBot:", response)