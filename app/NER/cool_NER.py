from app.preprocessing import cool_preproc
from app import gazetteer
import spacy


def is_gazetteer(cand):
    for name in gazetteer:
        if name == cand.text:
            return True


def spacy_cand(parsed):
    candidates = []
    for sent in parsed.sents:
        for entity in sent.ents:
            if entity.label_ == 'GPE':
                candidates.append(entity)
    return candidates


def rules_cand(sent):
    candidates = []

    def compound_recursion(sent, init_ind, ind):
        token = sent[ind]
        if token.pos_ == 'PROPN' and token.dep_ in ['pobj', 'appos']:
            return sent[init_ind:ind+1]
        elif token.pos_ == 'PROPN' and token.dep_ == 'compound':
            return compound_recursion(sent,  init_ind, ind+1)

    ind = 0
    while ind < len(sent):
        token = sent[ind]
        if token.pos_ == 'PROPN' and token.dep_ == 'pobj':
            candidates.append(token)
        if token.pos_ == 'PROPN' and token.dep_ == 'compound':
            compound = compound_recursion(sent, ind, ind+1)
            candidates.append(compound)
            ind += len(compound)-1
        ind += 1

    return candidates


def gazetteer_cand(parsed):
    candidates = []
    for chunk in parsed.noun_chunks:
        if chunk.root.dep_ == 'pobj':
            if is_gazetteer(chunk):
                candidates.append(chunk)
    return candidates

def chunk_cand(parsed):
    candidates = []
    for chunk in parsed.noun_chunks:
        if chunk.root.dep_ == 'pobj':
            if all([ token.text[0].isupper() for token in chunk ]):
                candidates.append(chunk)
    return candidates


def loc_relation(cand):
    if isinstance(cand, spacy.tokens.span.Span):
        cand = cand.root
    if cand.head.text == 'from':
        return 'from'
    elif cand.head.text == 'to':
        return 'to'
    else:
        return None


def extract(parsed):

    _from = None
    _to = None

    gazetteer_cands = gazetteer_cand(parsed)
    spacy_cands = spacy_cand(parsed)
    rules_cands = rules_cand(parsed)
    chunk_cands = chunk_cand(parsed)

    all_cands = [gazetteer_cands] + [spacy_cands] + [rules_cands] + [chunk_cands]

    for lst in all_cands:
        if lst:
            for cand in lst:
                if loc_relation(cand) == 'from':
                    _from = cand.text
                elif loc_relation(cand) == 'to':
                    _to = cand.text
                else:
                    continue

    return _from, _to


if __name__ == '__main__':
    # Test your stuff.

    s1 = 'from Lviv to New York'
    parsed = cool_preproc(s1)
    print(extract(parsed))
