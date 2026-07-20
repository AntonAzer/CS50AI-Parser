# CS50AI - Parser

## Overview
This project is part of the CS50's Introduction to Artificial Intelligence with Python course. The goal is to build an AI that can parse English sentences, understand their syntactic structure, and extract specific chunks of information (Noun Phrases) using Context-Free Grammar (CFG) and the Natural Language Toolkit (`nltk`).

## Features
- **Preprocessing:** Tokenizes input text into lowercase words, filtering out pure punctuation.
- **Syntactic Parsing:** Uses a custom-defined Context-Free Grammar (CFG) to parse standard English sentences.
- **Noun Phrase Chunking:** Analyzes the generated syntax trees to identify and extract Noun Phrase (NP) chunks (noun phrases that do not contain other noun phrases within them).

## Grammar Rules
The CFG is constructed using the following components:
- `S`: Sentence (composed of a Noun Phrase and a Verb Phrase, or two sentences joined by a conjunction).
- `NP`: Noun Phrase (can include determiners, adjectives, nouns, and prepositional phrases).
- `VP`: Verb Phrase (can include verbs, adverbs, noun phrases, and prepositional phrases).
- `AP`: Adjective Phrase (handles multiple adjectives modifying a noun).
- `PP`: Prepositional Phrase (preposition followed by a noun phrase).

## How to Run
To run the parser on a text file containing a sentence (e.g., `sentences/1.txt`):
```bash
python parser.py sentences/1.txt
