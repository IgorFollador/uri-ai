import requests
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# criação do chatbot
bot = ChatBot('Dica de Filme Bot')

# treinamento do chatbot com o corpus de conversas padrão
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.portuguese')

# criação da base de dados com informações sobre filmes e suas respectivas categorias
filmes = {
    'Ação': ['Vingadores: Guerra Infinita', 'John Wick', 'Velozes e Furiosos'],
    'Comédia': ['Se Beber, Não Case', 'Debi e Lóide', 'As Branquelas'],
    'Drama': ['O Poderoso Chefão', 'Forrest Gump', 'A Lista de Schindler'],
    'Romance': ['Titanic', 'Diário de uma Paixão', 'Como Eu Era Antes de Você']
}

# função que retorna a nota do filme no Rotten Tomatoes
# def get_rotten_tomatoes_score(filme):
#     api_key = 'sua_api_key_do_rotten_tomatoes'
#     url = f'http://www.omdbapi.com/?t={filme}&apikey={api_key}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         if 'Ratings' in data:
#             for rating in data['Ratings']:
#                 if rating['Source'] == 'Rotten Tomatoes':
#                     return int(rating['Value'].replace('%', ''))
#     return 0
def get_rotten_tomatoes_score(filme):
    api_key = '8bb6f050'
    url = f'http://www.omdbapi.com/?t={filme}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Ratings' in data:
            for rating in data['Ratings']:
                if rating['Source'] == 'Rotten Tomatoes':
                    return int(rating['Value'].replace('%', ''))
    return 0

# função que retorna o filme com a nota mais alta na categoria
def dica_de_filme(categoria):
    if categoria in filmes:
        notas = {}
        for filme in filmes[categoria]:
            notas[filme] = get_rotten_tomatoes_score(filme)
        melhor_filme = max(notas, key=notas.get)
        return melhor_filme
    else:
        return "Desculpe, não encontrei filmes nessa categoria. Por favor, tente novamente."

# loop que solicita ao usuário uma categoria e retorna um filme
while True:
    try:
        user_input = input("Você: ")
        response = bot.get_response(user_input)
        if float(response.confidence) > 0.0:
            categoria = response.text
            filme = dica_de_filme(categoria)
            print(f"Bot: Que tal assistir '{filme}'?")
        else:
            print("Bot: Desculpe, não entendi. Pode me explicar melhor?")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break