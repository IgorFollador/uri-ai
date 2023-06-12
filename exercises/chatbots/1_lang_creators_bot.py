# TODO: Inform the creator and year of creation of a strong user programming language (at least 10 languages)

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('Scoot')

trainer = ListTrainer(chatbot)
# trainer = ChatterBotCorpusTrainer(chatbot)

# trainer.train('chatterbot.corpus.portuguese')

sentences = [
    'Quem criou a linguagem Python?', 'O criador foi Guido van Rossum',
    'Quem criou a linguagem PHP?', 'O criador foi Rasmus Lerdorf',
    'Quem criou a linguagem Java?', 'O criador foi James Gosling',
    'Quem criou a linguagem C?', 'O criador foi Dennis Ritchie',
    'Quem criou a linguagem C++?', 'O criador foi Bjarne Stroustrup',
    'Quem criou a linguagem C#?', 'O criador foi Anders Hejlsberg',
    'Quem criou a linguagem Pascal?', 'O criador foi Niklaus Wirth',
    'Quem criou a linguagem Lua?', 'O criador foi Roberto Ierusalimschy',
    'Quem criou a linguagem Ruby?', 'O criador foi Yukihiro Matsumoto',
    'Quem criou a linguagem Javascript?', 'O criador foi Brendan Eich',
]

trainer.train(sentences)

while True:
    answer = input("You: ")
    response = chatbot.get_response(answer)

    if float(response.confidence) > 0.5:
        print('Bot Scoot:', response)
    else:
        print('Bot Scoot: Me desculpe, não consegui entender!')