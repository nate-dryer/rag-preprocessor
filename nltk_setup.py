import nltk
import logging

def download_nltk_resources():
    # List of NLTK resources required for the script to function
    resources = [
        'averaged_perceptron_tagger',
        'punkt',
        'wordnet',
        'maxent_ne_chunker',
        'words'
    ]

    for resource in resources:
        try:
            # Check if the resource is already installed
            nltk.data.find(resource)
            logging.info(f"NLTK resource '{resource}' is already installed.")
        except LookupError:
            # Resource is not installed, so attempt to download it
            logging.info(f"Downloading NLTK resource '{resource}'.")
            nltk.download(resource)