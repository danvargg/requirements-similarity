"""Calculate the similarity between user business requirements."""
import os
import string
import warnings

import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings('ignore')

# Processors
STEMMER = nltk.stem.porter.PorterStemmer()
LEMMER = nltk.stem.WordNetLemmatizer()
REMOVE_PUNC_DICT = dict((ord(punct), None) for punct in string.punctuation)


def lem_tokens(tokens: list) -> list:
    """
    Lemmatize tokens.
    Args:
        tokens: Tokens to lemmatize.

    Returns:
        Lemmatized tokens.
    """
    return [LEMMER.lemmatize(token) for token in tokens]


def lem_normalize(text: str) -> list:
    """
    Lemmatize and normalize text.
    Args:
        text: Text to lemmatize.

    Returns:
        Lemmatized and normalized text.
    """
    return lem_tokens(nltk.word_tokenize(text.lower().translate(REMOVE_PUNC_DICT)))


def cos_similarity(text_list):
    """
    Calculate cosine similarity.
    Args:
        text_list: List of text to calculate similarity.

    Returns:
        Cosine similarity.
    """
    # print(type(text_list))
    tfidf_vect = TfidfVectorizer(tokenizer=lem_normalize, stop_words='english')
    tfidf = tfidf_vect.fit_transform(text_list.astype('U'))
    return (tfidf * tfidf.T).toarray()


# Constants
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
COLUMNS = ['Requirement ID', 'Description', 'So that']

# Data preparation
data = pd.read_excel(open(os.path.join(DATA_PATH, 'rtm.xlsx'), 'rb'), sheet_name='L1 Requirements')

data = data[COLUMNS]
data.rename(
    columns={
        'Requirement ID': 'req_id',
        'So that': 'so_that'
    }, inplace=True
)

data['requirement'] = data['Description'] + data['so_that']
data = data[['req_id', 'requirement']]
data['requirement'] = data['requirement'].str.lower()
data['requirement'] = data.requirement.str.replace('i want ', '')
data['requirement'] = data.requirement.str.replace('so that ', '')

reqs = data['requirement'].values

# Calculate similarity
us_similarity = pd.DataFrame(cos_similarity(reqs))
us_similarity = us_similarity.dropna()

us_similarity.index = data['req_id']
us_similarity.columns = data['req_id']

print(us_similarity)
