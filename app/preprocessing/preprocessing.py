import nltk
import spacy
from nltk import Tree
from spacy import displacy

cool_parser = spacy.load('en')
wnl = nltk.WordNetLemmatizer()
# pip install spacy
# python -m spacy download en


def preproc(text):
    parsed = []
    sent_text = nltk.sent_tokenize(text)
    for sent in sent_text:
        tokenized_text = nltk.word_tokenize(sent)
        pos = nltk.pos_tag(tokenized_text)
        parsed.append([(wnl.lemmatize(word[0]), word[1]) for word in pos])
    return parsed


def cool_preproc(text):
    return cool_parser(text)


if __name__ == '__main__':
    # Test your stuff.
    s = 'I am flying from Lviv to New York.'
    print(preproc(s))
    parsed = cool_parser(s)
    displacy.serve(parsed, style='dep')
