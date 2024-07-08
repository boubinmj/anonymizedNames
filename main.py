import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
text = "Hello, how are you doing?"
tokens = word_tokenize(text)
print(tokens)