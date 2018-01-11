import nltk
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def tokenize(sent):
    return word_tokenize(sent)

def remove_stop_words(tokens):
    return [token for token in tokens if token not in stopwords.words('english')]

def categorize(tokens, categories):
    tokens = nltk.pos_tag(tokens)
    return [token[0] for token in tokens if token[1] in categories]

def porter_stem(tokens):
    ps = PorterStemmer()
    return [ps.stem(token) for token in tokens]

def process_input(arg):
    tokens = porter_stem(categorize(remove_stop_words(tokenize(arg)), ['JJ', 'RB', 'RBR', 'RBS', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJR', 'JJS', 'VB', 'NN', 'NNP','NNPS']))
    return list(set(tokens))