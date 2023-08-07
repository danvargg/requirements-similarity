"""Calculate the similarity between user business requirements."""
import os
import string

import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

from text_processing import TextProcessor

# os.chdir('C:/Users/devg2/Downloads')

data = pd.read_excel(open('jira.xlsx', 'rb'))
data = data[['Issue key', 'Description', 'Issue Type', 'Custom field (Requirement ID)']]
data['Issue_Type'] = data['Issue Type']
data = data[data.Issue_Type == 'Story']

data = data.dropna(how='all')

data['Description'] = data.Description.str.replace('I want ', '')
data['Description'] = data.Description.str.replace('so that ', '')
req = data[['Issue key', 'Description']]

reqs = req['Description'].values

stemmer = nltk.stem.porter.PorterStemmer()


def StemTokens(tokens):
    return [stemmer.stem(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def StemNormalize(text):
    return StemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


''' Matrix'''

TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')


def cos_similarity(textlist):
    tfidf = TfidfVec.fit_transform(textlist.astype('U'))
    return (tfidf * tfidf.T).toarray()


# filter similarity > 0.5

us_similarity = pd.DataFrame(cos_similarity(reqs))

# nulls = us_similarity.isnull().any()

''' name columns and rows '''

us_similarity.index = req['Issue key']
us_similarity.columns = req['Issue key']

us_similarity.to_csv('us_similarity.csv', sep=',')
