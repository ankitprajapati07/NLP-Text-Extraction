import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Download the required NLTK resources (you can run this once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def pos_tagging(text):

    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    return pos_tags


input_text = "ENTER YOUR TEXT HERE"
result_pos_tags = pos_tagging(input_text)
print(result_pos_tags)
