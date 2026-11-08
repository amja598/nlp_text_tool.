# NLP Text Analysis Tool

# 1. Project Overview

This project is a beginner-level Natural Language Processing (NLP) tool developed using Python and the spaCy library.

Its purpose is to explore some fundamental concepts and techniques in Computational Linguistics by applying them to written text. The program allows users to process text from local files or webpages and perform several types of linguistic and NLP analysis.

The project was developed as an independent learning exercise to gain practical experience with Python, NLP libraries, and computational approaches to language analysis.

It is an introductory project rather than an original NLP system or a contribution of new algorithms. It relies on existing tools, pretrained models, and established NLP techniques.

# 2. Features

The program currently provides the following functionalities:

# A. Text Input and Processing

Users can choose between two methods of providing text:

- Local files: The program reads and processes text files using UTF-8 encoding.
- Webpages: Users can provide a URL, and the program retrieves the webpage, extracts its text using BeautifulSoup, and removes script and style elements before processing.

The extracted text is then processed using spaCy's English NLP pipeline.

# B. Part-of-Speech (POS) Tagging

The program identifies the grammatical category of individual tokens in a text.

Examples include:
- Nouns
- Verbs
- Adjectives
- Adverbs
- Pronouns
- Determiners
- Prepositions

This feature uses spaCy's pretrained linguistic pipeline to assign POS tags to tokens.

# C. Named Entity Recognition (NER)

The program identifies named entities within the processed text and displays their corresponding labels.

It uses spaCy's existing Named Entity Recognition component to identify entities such as organizations, locations, and other recognized categories.

# D. Rule-Based Entity Recognition

In addition to the pretrained NER component, the project incorporates spaCy's EntityRuler.

This component allows manually defined patterns to identify specific entities.

For example, a collection of capital cities and organizations has been added through predefined patterns.

The manually defined patterns include:
- Capital cities, such as Paris, Tokyo, Rabat, and London.
- Organizations, such as Google, Microsoft, Apple, and OpenAI.

These patterns allow the program to recognize certain entities based on predefined linguistic rules.

# E. Dependency Parsing Visualization

The program provides an option to visualize the grammatical relationships between words using spaCy's DisplaCy visualization tool.

Dependency parsing represents the syntactic relationships between tokens, illustrating how individual words relate to one another within a sentence.

The visualization is served locally through a web browser.

# F. Word Similarity

The project also includes a basic word similarity feature using spaCy's pretrained word vectors.

Users can enter a word and compare it with the tokens in the processed text.

The program calculates similarity scores and displays words whose scores exceed a predefined threshold of 0.49.

This feature provides a basic introduction to distributional semantics and the use of word vectors in NLP.

# 3. Technologies and Libraries

The project uses the following technologies:


- Python : Main programming language 
- spaCy : Natural Language Processing 
- en_core_web_md : Pretrained English NLP model with word vectors 
- BeautifulSoup4 : HTML parsing and text extraction 
- urllib : Retrieving webpage content 
- DisplaCy : Dependency parsing visualization 

# 4. Installation and Requirements

# Requirements

- Python 3
- spaCy
- BeautifulSoup4
- Internet connection for webpage processing

# Installation

Install the required libraries:

pip install spacy beautifulsoup4


Download the English medium-sized spaCy model:

python -m spacy download en_core_web_md

# Running the Program

Save the Python script and run it from your terminal:

python your_script.py

Replace 'your_script.py' with the actual name of the Python file.

Follow the instructions displayed in the terminal to select the desired analysis options.

# 5. How to Use

When the program starts, users are presented with three options:

- 'file': Process a local text file.
- 'web': Retrieve and process text from a webpage.
- 'exit': Terminate the program.

After processing the text, users can:

1. Choose whether to visualize the dependency parsing diagram.
2. Display named entity labels or POS tags.
3. Check word similarity by entering a word.
4. Continue processing another document or exit.

# 6. Limitations 

This project has several limitations that should be considered.

- Limited entity patterns: The manually defined entity patterns cover a relatively small collection of capital cities and organizations.
- Pretrained model dependency: Most linguistic analysis relies on spaCy's existing pretrained English model rather than a model trained specifically for this project.
- Basic similarity analysis: The similarity feature uses a fixed threshold and does not rank results or filter out all irrelevant words.
- Basic webpage extraction: The webpage processing component extracts general HTML text but does not reliably distinguish the main article from navigation elements, advertisements, and other page content.
- Language limitation: The current implementation is designed for English text.
- Terminal-based interface: The program operates through a command-line interface and does not include a graphical user interface.
- Limited testing: The project has not undergone extensive automated testing or evaluation against linguistic benchmarks.

# 7. Learning Objectives and Project Motivation

The main motivation behind this project was to gain practical exposure to Natural Language Processing and explore how linguistic information can be represented and analyzed computationally.

Coming from an English Linguistics background, I wanted to explore the relationship between theoretical linguistic knowledge and computational methods.

Through this project, I gained introductory experience with:

- Python programming and external libraries.
- Text processing and tokenization.
- Morphosyntactic analysis through POS tagging.
- Named Entity Recognition and rule-based approaches.
- Syntactic analysis through dependency parsing.
- Word vectors and semantic similarity.
- Processing text from different sources.

The project represents an initial step in my exploration of Computational Linguistics and NLP.

# 8. Acknowledgements

This project relies on the spaCy library and its existing NLP pipeline, including the 'en_core_web_md' model.

It also uses BeautifulSoup for HTML parsing and DisplaCy for linguistic visualization.

The implementation was developed as an independent learning exercise using publicly available Python libraries and their documentation.

