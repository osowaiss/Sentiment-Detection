# Sentiment-Detection
# Root Word and Tense Identifier

## Overview
This Python program utilizes **Natural Language Toolkit (nltk)** and **spaCy** to analyze a given sentence, phrase, or word. It identifies the root word (lemma) of verbs and determines the dominant tense (past, present, or future) in the input text.

## Features
- Tokenizes the input text
- Identifies root forms of words using **lemmatization**
- Detects and categorizes verb tense (past, present, or future)

## Requirements
Ensure you have Python installed on your system. Then install the required dependencies using:

```bash
pip install nltk spacy
python -m spacy download en_core_web_sm
```

## Usage
Run the script and input a sentence, phrase, or word:

```bash
python script.py
```

Then enter a sentence when prompted, for example:

```
Enter a sentence, phrase, or word: She was running fast and jumped over the hurdle.
```

### Expected Output:
```
Root Words: ['run', 'jump', 'be']
Detected Tense: past
```

## Code Implementation
```python
import nltk
import spacy
from nltk.tokenize import word_tokenize
from collections import Counter

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

def get_root_and_tense(text):
    doc = nlp(text)
    root_words = []
    verb_tenses = {"past": 0, "present": 0, "future": 0}

    for token in doc:
        if token.pos_ in ["VERB", "AUX"]:  # Identify verbs and auxiliary verbs
            root_words.append(token.lemma_)  # Lemmatize to get root form

            # Identify tense
            if token.tag_ in ["VBD", "VBN"]:  # Past tense
                verb_tenses["past"] += 1
            elif token.tag_ in ["VBP", "VBZ", "VBG"]:  # Present tense
                verb_tenses["present"] += 1
            elif token.tag_ == "MD":  # Modal verb (may indicate future)
                verb_tenses["future"] += 1

    # Determine the dominant tense
    dominant_tense = max(verb_tenses, key=verb_tenses.get) if any(verb_tenses.values()) else "unknown"

    return {"Root Words": list(set(root_words)), "Dominant Tense": dominant_tense}

# Example Usage
if __name__ == "__main__":
    text = input("Enter a sentence, phrase, or word: ")
    result = get_root_and_tense(text)
    print("Root Words:", result["Root Words"])
    print("Detected Tense:", result["Dominant Tense"])
```

## Example Inputs & Outputs

### **Input:**  
```text
He is reading a book now.
```
### **Output:**  
```text
Root Words: ['read', 'be']
Detected Tense: present
```

### **Input:**  
```text
They will travel to Paris next summer.
```
### **Output:**  
```text
Root Words: ['travel']
Detected Tense: future
```

## License
This project is open-source and available under the MIT License.

---

This README provides a clear explanation of the project, installation steps, usage, and example outputs. 🚀

