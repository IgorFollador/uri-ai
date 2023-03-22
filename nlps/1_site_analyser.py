import nltk
import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# Get all words witch doesn't add much meaning
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

# Get html data by request
response = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Telesc%C3%B3pio_espacial_Hubble')
html = response.read()
webscrap = BeautifulSoup(html, 'html5lib')

# Cut text in words and change all content to lower
content = webscrap.get_text(strip = True)
content = content.lower()

content = re.sub(r'[^\w\s]', ' ', content)
content = re.sub("\d", ' ', content)

text_words = [t for t in content.split()]

acceptable_words = []

for word in text_words:
    if word not in stopwords and len(word) < 30 and len(word) > 3:
        acceptable_words.append(word)

freq_words = nltk.FreqDist(acceptable_words)

for index, value in freq_words.items():
    print('Word[' + str(index) + ']:' + str(value))

freq_words.plot(5)