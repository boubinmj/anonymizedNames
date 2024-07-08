import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def salesforce_login():
    from credentials_connection import User
    conn = User('dev')
    conn.getCredentials()
    sf = conn.sf_login()
    return sf


sf = salesforce_login()

text = "Hello, how are you doing?"
tokens = word_tokenize(text)
print(tokens)