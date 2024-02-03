import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download the required NLTK resources (you can run this once)
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def count_named_entity_frequency(text):

    try:
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        named_entities = ne_chunk(pos_tags)

        # Extract named entities and count their frequency
        named_entity_list = []
        for subtree in named_entities:
            if isinstance(subtree, nltk.Tree):
                entity = " ".join([token[0] for token in subtree.leaves()])
                named_entity_list.append(entity)

        frequency_distribution = FreqDist(named_entity_list)
        return frequency_distribution
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


input_text = "ENTER YOUR TEXT HERE"
entity_frequency = count_named_entity_frequency(input_text)

# Check if the result is valid
if entity_frequency is not None:

    for entity, count in entity_frequency.items():
        print(f"{entity}: {count} times")
else:
    print("Error in processing named entities.")
