# Rag File Preprocessor

This tool preprocesses text files for RAG-based information retrieval. It utilizes operations from the Natural Language Toolkit (NLTK), such as tokenization, part-of-speech tagging, named entity recognition, and lemmatization. 

## Key Features

- **Tokenization**: Splits text into tokens (words and sentences).
- **Part-of-Speech Tagging**: Assigns parts of speech to each token, such as verb, noun, adjective, etc.
- **Named Entity Recognition**: Identifies and classifies named entities in text into predefined categories.
- **Lemmatization**: Reduces words to their base or dictionary form.
- **Phone Number Extraction and Anonymization**: Detects and anonymizes phone numbers in text.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- Python 3.x
- Natural Language Toolkit (NLTK)

You can install NLTK using pip: 

```pip install nltk```

## Installation

Clone the repository to your local machine to get started:

```
git clone https://github.com/nate-dryer/rag-preprocessor.git
cd  <project_directory>
```

## Usage

Run the script using the following command:

```
python main.py <input_file> --format <output_format> --logging
```

Replace `<input_file>` with the path to your text file, and `<output_format>` with either `json` or `csv` depending on your desired output format.

## Contributing

Contributions to the Text Preprocessing Utility are welcome!

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with a detailed description of your changes.

## Contact  

- **Nathan Dryer**
- GitHub: [nate-dryer](https://github.com/nate-dryer)
- Website: [https://natedryer.com](https://natedryer.com)  

## License

This project is licensed under the MIT License - for more information, refer to the LICENSE file.
