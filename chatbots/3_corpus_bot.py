from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('FolaBot')

# Mount the trainer based in a "corpus"
trainer = ChatterBotCorpusTrainer(chatbot)

# Define the corpus to portuguese
trainer.train('chatterbot.corpus.portuguese')

# Export the file with the trained content
trainer.export_for_training('./data.json')