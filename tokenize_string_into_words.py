import nltk
from nltk.tokenize import word_tokenize

# Download the required NLTK resources (you can run this once)
nltk.download('punkt')


def tokenize_text(text):

    tokens = word_tokenize(text)
    return tokens


input_text = "ENTER YOUR TEXT HERE"
result_tokens = tokenize_text(input_text)
print(result_tokens)
