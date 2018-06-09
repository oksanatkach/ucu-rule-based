import nltk

wnl = nltk.WordNetLemmatizer()


def preproc(text):
    parsed = []
    sent_text = nltk.sent_tokenize(text)
    for sent in sent_text:
        tokenized_text = nltk.word_tokenize(sent)
        pos = nltk.pos_tag(tokenized_text)
        parsed.append([(wnl.lemmatize(word[0]), word[1]) for word in pos])
    return parsed


if __name__ == '__main__':
    # Test your stuff.
    s = 'This is a sample text. It contains two sentences.'
    print preproc(s)
