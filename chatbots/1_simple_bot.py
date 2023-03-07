from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new Chatbot called FolaBot
chatbot = ChatBot('FolaBot')

# Create a "trainer" to FolaBot
trainer = ListTrainer(chatbot)

conversation = ['Olá', 'Olá, tudo bem?', 'Tudo bem?', 
                'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

# Execute the train FolaBot with the words/sentences
trainer.train(conversation)

# Loop for the conversation to happen
while True:
    # Input user data
    answer = input("Usúario: ");
    # Search a FolaBot response
    response = chatbot.get_response(answer)

    if float(response.confidence) > 0.5:
        print('FolaBot: ', response)
    else:
        print("FolaBot: Me desculpe! Não tenho uma resposta para essa pergunta.")