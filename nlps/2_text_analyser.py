import nltk
import re

# Get all words witch doesn't add much meaning
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

file = open('text.txt', 'r+', encoding="utf8")
content = file.read()
content = content.lower()

content = re.sub(r'[^\w\s]', ' ', content)
content = re.sub("\d+", ' ', content)

text_words = [t for t in content.split()]

acceptable_words = []

for word in text_words:
    if word not in stopwords and len(word) < 30 and len(word) > 3:
        acceptable_words.append(word)

freq_words = nltk.FreqDist(acceptable_words)

for index, value in freq_words.items():
    print('Word[' + str(index) + ']:' + str(value))

freq_words.plot(5)