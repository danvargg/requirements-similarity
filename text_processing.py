"""Text processing functionalities."""
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer


def cos_similarity(textlist):
    tfidf = TfidfVectorizer.fit_transform(textlist.astype('U'))
    return (tfidf * tfidf.T).toarray()


class TextProcessor:
    """Text processing functionalities."""

    def __init__(self, text: pd.Series):
        """Initialize the text processor."""
        self.text = text
        self.stemmer = nltk.stem.porter.PorterStemmer()
        self.lemmer = nltk.stem.WordNetLemmatizer()

    def StemTokens(self, tokens):
        return [self.stemmer.stem(token) for token in tokens]

    def StemNormalize(self, text):
        return self.StemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    def LemTokens(self, tokens):
        return [self.lemmer.lemmatize(token) for token in tokens]

    def LemNormalize(self, text):
        return self.LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    def process_text(self):
        """Process the text."""
        self.remove_punctuation()
        self.remove_stopwords()
        self.lemmatize()
        self.stem()

    def remove_punctuation(self):
        """Remove punctuation from the text."""
        self.text = self.text.replace('.', '')
        self.text = self.text.replace(',', '')
        self.text = self.text.replace(';', '')
        self.text = self.text.replace(':', '')
        self.text = self.text.replace('!', '')
        self.text = self.text.replace('?', '')
        self.text = self.text.replace('(', '')
        self.text = self.text.replace(')', '')
        self.text = self.text.replace('[', '')
        self.text = self.text.replace(']', '')
        self.text = self.text.replace('{', '')
        self.text = self.text.replace('}', '')
        self.text = self.text.replace('"', '')
        self.text = self.text.replace("'", '')
        self.text = self.text.replace('`', '')
        self.text = self.text.replace('´', '')
        self.text = self.text.replace('’', '')
        self.text = self.text.replace('‘', '')
        self.text = self.text.replace('“', '')
        self.text = self.text.replace('”', '')
        self.text = self.text.replace('…', '')
        self.text = self.text.replace('–', '')
        self.text = self.text.replace('-', '')
        self.text = self.text.replace('_', '')
        self.text = self.text.replace('—', '')
        self.text = self.text.replace('/', '')
        self.text = self.text.replace('\\', '')
        self.text = self.text.replace('|', '')
        self.text = self.text.replace('«', '')
        self.text = self.text.replace('»', '')
        self.text = self.text.replace('°', '')
        self.text = self.text.replace('º', '')
