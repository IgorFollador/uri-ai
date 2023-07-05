import nltk
import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# Get all words that don't add much meaning
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

# URL
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
url = "https://www.tabnews.com.br"

# Get html data by request
req = Request(url=url, headers=headers)
html = urlopen(req).read()
webscrap = BeautifulSoup(html, 'html5lib')

# Cut text in words and change all content to lower
content = webscrap.get_text(strip=True)
content = content.lower()

content = re.sub(r'[^\w\s]', ' ', content)
content = re.sub(r"\d", ' ', content)

text_words = [t for t in content.split() if t]

acceptable_words = []

for word in text_words:
    if word not in stopwords and len(word) < 30 and len(word) > 3:
        acceptable_words.append(word)

freq_words = nltk.FreqDist(acceptable_words)

# Subject
palavra = input("Palavra: ")

# Filter words based on the given subject
filtered_words = [word for word in freq_words if palavra.lower() in word]

if filtered_words:
    for word in filtered_words:
        print(f'Word: {word}, Frequency: {freq_words[word]}')
else:
    print("No relevant words found.")

freq_words.plot(5)