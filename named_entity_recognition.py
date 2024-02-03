import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize

# Download the required NLTK resources (you can run this once)
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def named_entity_recognition(text):

    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags)
    return named_entities


input_text = "ENTER YOUR TEXT HERE."
result_ner = named_entity_recognition(input_text)
print(result_ner)
