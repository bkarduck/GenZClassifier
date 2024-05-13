# Generation Z Slang Classifier

## Overview

This project develops a natural language processing (NLP) model to classify and interpret Generation Z slang. The project leverages the spaCy library, particularly its powerful pipeline features, to process and analyze text data efficiently. The primary goal is to accurately identify and categorize Generation Z slang terms within larger text corpora, aiding in understanding the unique linguistic patterns and expressions of this demographic. One useful application of such a classifier is to be able to identify if a sentence likely came from a younger person or older individual; this may be used in optimizing chat bots in business situations to adjust to talking similar to whoever their audience is.

## Features

Slang Identification: Detects and highlights slang terms used by Generation Z (features spaCy NER).

Contextual Understanding: Interprets slang within the context it's used (in this case, I used reddit posts from a teenagers thread and reddit posts from an adult advice thread) to provide accurate meanings.

Custom spaCy Pipeline: Integrates custom components into the spaCy pipeline for tailored processing of Generation Z slang.

Model Training & Evaluation: Involves training the roBERTa classifier through spaCy with annotated datasets and evaluating its performance.

Interactive Interface: A CLI for testing and interacting with the classifier.

