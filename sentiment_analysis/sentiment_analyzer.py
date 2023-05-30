from textblob import TextBlob
from googletrans import Translator
import matplotlib.pyplot as plt

def percentage(part, total):
    return 100*float(part)/float(total)

def translate(sentence):
    translator = Translator()
    sentenceTranslated = translator.translate(sentence, src='pt', dest='en').text
    return sentenceTranslated

positive = 0
negative = 0
neutral = 0
polarity = 0

contents = []
contents.append(TextBlob(translate("O governo anunciou hoje uma nova política econômica que visa impulsionar o crescimento do país, gerando empregos e estimulando o investimento no setor produtivo, o que traz esperança de uma recuperação econômica significativa nos próximos meses, levando otimismo aos mercados financeiros e à população em geral.")));
contents.append(TextBlob(translate("Um trágico acidente ocorreu esta manhã, envolvendo um ônibus escolar e um caminhão na rodovia principal da cidade.")));
contents.append(TextBlob(translate("Uma nova pesquisa científica revelou descobertas surpreendentes sobre os efeitos do sono na saúde mental. O estudo indica que a privação crônica de sono está diretamente relacionada ao aumento dos índices de ansiedade e depressão, levantando questões sobre a importância de uma boa qualidade de sono e promovendo debates sobre políticas públicas de saúde mental.")));
contents.append(TextBlob(translate("A chegada de uma nova vacina contra uma doença altamente contagiosa trouxe alívio e esperança para a população mundial, especialmente em meio à pandemia global em curso. A nova vacina passou por rigorosos testes clínicos e obteve resultados promissores, levando a comunidade científica a acreditar que estamos mais perto de controlar e superar essa crise de saúde pública.")));

for sentence in contents:
    polarity += sentence.sentiment.polarity
    print(sentence, "\n", sentence.sentiment, '\n')
    
    if (sentence.sentiment.polarity == 0):
        neutral += 1
    elif (sentence.sentiment.polarity < 0):
        negative += 1
    elif (sentence.sentiment.polarity > 0):
        positive += 1

positive = format(percentage(positive, len(contents)), '.2f')
negative = format(percentage(negative, len(contents)), '.2f')
neutral = format(percentage(neutral, len(contents)), '.2f')

labels = ['Positivo [' + str(positive) +'%]', 'Neutro [' + str(neutral) +'%]', 'Negative [' + str(negative) +'%]']

sizes = [positive, neutral, negative]

colors = ['green', 'lightgray', 'red']

patches,texts = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()