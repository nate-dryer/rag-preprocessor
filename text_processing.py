import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk import pos_tag, ne_chunk
import logging

# Function to get the WordNet POS tag
def get_wordnet_pos(treebank_tag):
    return {
        'J': wordnet.ADJ,
        'V': wordnet.VERB,
        'N': wordnet.NOUN,
        'R': wordnet.ADV
    }.get(treebank_tag[0], wordnet.NOUN)

# Function to normalize text to lowercase
def normalize_text(input_text):
    return input_text.lower()

# Function to process text using NLP techniques
def process_text(input_text):
    lemmatizer = nltk.WordNetLemmatizer()
    input_text = normalize_text(input_text)
    tokens = word_tokenize(input_text)
    
    try:
        pos_tags = pos_tag(tokens)
        ner_tree = ne_chunk(pos_tags)
    except Exception as e:
        logging.error(f"Error during NLP processing: {e}")
        return input_text

    processed_words = []
    for item in ner_tree:
        if hasattr(item, 'label') and item.label():
            entity_name = ' '.join(c[0] for c in item.leaves())
            processed_words.append(entity_name)
        else:
            word, pos = item
            wordnet_pos = get_wordnet_pos(pos)
            lemmatized_word = lemmatizer.lemmatize(word, wordnet_pos)
            processed_words.append(lemmatized_word)
    
    return ' '.join(processed_words)