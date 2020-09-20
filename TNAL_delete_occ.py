
from nltk.corpus import stopwords
stopwords= set(stopwords.words('french'))
clean_words = []
for token in return_token(test):
    if token not in stopwords:
        clean_words.append(token)

clean_words
