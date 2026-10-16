import nltk
import string

# Download required NLTK datasets
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("maxent_ne_chunker_tab")
nltk.download("words")

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
from nltk import pos_tag, ne_chunk

# Input text
text = input("Enter a paragraph:\n")

# 1. Sentence Tokenization
sentences = sent_tokenize(text)
print("\n1. Sentences:")
print(sentences)

# 2. Word Tokenization
words = word_tokenize(text)
print("\n2. Words:")
print(words)

# 3. Count Words
print("\n3. Total Words:", len(words))

# 4. Remove Punctuation
clean_words = [
    word.lower() for word in words
    if word not in string.punctuation
]
print("\n4. Without Punctuation:")
print(clean_words)

# 5. Remove Stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [
    word for word in clean_words
    if word not in stop_words
]
print("\n5. Without Stopwords:")
print(filtered_words)

# 6. Stemming
stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in filtered_words]
print("\n6. Stemming:")
print(stems)

# 7. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in filtered_words]
print("\n7. Lemmatization:")
print(lemmas)

# 8. Part-of-Speech Tagging
tags = pos_tag(words)
print("\n8. POS Tagging:")
print(tags)

# 9. Word Frequency
frequency = FreqDist(filtered_words)
print("\n9. Word Frequency:")
print(frequency.most_common(10))

# 10. Named Entity Recognition
print("\n10. Named Entities:")
tagged_words = pos_tag(words)
entities = ne_chunk(tagged_words)
print(entities)

# 11. Find words containing a specific substring
search_word = input("\nEnter substring to search: ").lower()
matches = [
    word for word in clean_words
    if search_word in word
]
print("Matching words:", matches)

# 12. Display unique words
print("\n12. Unique Words:")
print(sorted(set(clean_words)))