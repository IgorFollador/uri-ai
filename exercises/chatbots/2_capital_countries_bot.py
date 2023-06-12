# TODO: Inform the capital of a country entered by the user (at least 15 countries)

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('Scoot')

trainer = ListTrainer(chatbot)
# trainer = ChatterBotCorpusTrainer(chatbot)

# trainer.train('chatterbot.corpus.portuguese')

sentences = [
    'Qual a capital do Brasil?', 'Brasília',
    'Qual a capital da Alemanha?', 'A capital da Alemanha é Berlim',
    'Qual a capital dos Estados Unidos?', 'Washington, D.C.',
    'Qual a capital do Japão?', 'Tóquio',
    'Qual a capital da França?', 'A capital da França é Paris',
    'Qual a capital da Rússia?', 'Moscou',
    'Qual a capital do Canadá?', 'Ottawa',
    'Qual a capital da Austrália?', 'A capital da Austrália é Canberra',
    'Qual a capital da China?', 'Pequim',
    'Qual a capital do México?', 'Cidade do México',
    'Qual a capital da Itália?', 'Roma',
    'Qual a capital da Espanha?', 'Madri',
    'Qual a capital do Reino Unido?', 'Londres',
    'Qual a capital da Índia?', 'Nova Delhi',
    'Qual a capital da Argentina?', 'Buenos Aires',
    'Qual a capital da África do Sul?', 'Pretória, Cidade do Cabo e Bloemfontein (três capitais)',
    'Qual a capital do Egito?', 'Cairo',
    'Qual a capital da Turquia?', 'Ancara',
    'Qual a capital da Coreia do Sul?', 'Seul',
    'Qual a capital da Suécia?', 'Estocolmo'
]

trainer.train(sentences)

while True:
    answer = input("You: ")
    response = chatbot.get_response(answer)

    if float(response.confidence) > 0.5:
        print('Bot Scoot:', response)
    else:
        print('Bot Scoot: Me desculpe, não consegui entender!')