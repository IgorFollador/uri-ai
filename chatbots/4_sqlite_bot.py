from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new Chatbot called FolaBot
chatbot = ChatBot('FolaBot',
        logic_adapters=[
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.TimeLogicAdapter"
        ],
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite0'
        )

# Loop for the conversation to happen
while True:
    # Input user data
    answer = input("User: ");
    # Search a FolaBot response
    response = chatbot.get_response(answer)

    if float(response.confidence) > 0.5:
        print('FolaBot: ', response)
    else:
        print("FolaBot: I`m sorry! I don`t have response to your answer.")