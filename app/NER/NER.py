from app.preprocessing import preproc
from app import gazetteer

def isloc(raw, ind, sent, lemma, pos):

    for name in gazetteer:
        if name.split()[0] == lemma:
            return True

    if pos == 'NNP' and sent[ind-1][1] in ['IN', 'TO']:
        return True

    elif pos == 'NNP':# and sent[ind+1][0] == '-':
        return True

    elif 'city' in raw.lower():
        return True

    elif 'town' in raw.lower():
        return True

    elif lemma[0].isupper() and pos == "NN":
        return True


def NER_recursion(ind, sent, lemma, pos):

    if ind+1 == len(sent):
        return lemma
    elif sent[ind+1][1] != pos:
        return lemma
    elif sent[ind+1][0].islower():
        return lemma
    else:
        lemma = lemma + ' ' + sent[ind+1][0]
        return NER_recursion(ind+1, sent, lemma, pos)


def find_loc(locs, raw, parsed):
    # for sent in parsed:
    for ind in range(len(parsed)):
        el = parsed[ind]
        lemma = el[0]
        pos = el[1]
        if isloc(raw, ind, parsed, lemma, pos):
            name = NER_recursion(ind, parsed, lemma, pos)
            if locs != []:
                locs.append(( locs[-1][0] + len(locs[-1][1].split()) + ind, name))
            else:
                locs.append((ind, name))
            return find_loc(locs, raw, parsed[ind+len(name.split()):])
    return locs


def loc_relation(loc, parsed):
    prev_w = ''
    next_w = ''
    if loc[0] >= 0:
        prev_w = parsed[loc[0]-1][0]
    if loc[0]+1 != len(parsed):
        next_w = parsed[loc[0]+1][0]

    if prev_w in ['from', 'leave', 'leaving'] or next_w == '-':
        return 'from'
    elif prev_w in ['to', 'into', 'towards', '-']:
        return 'to'


if __name__ == '__main__':
    # Test your stuff.

    s1 = 'I am flying from Lviv to New York'
    parsed = preproc(s1)
    locs = [find_loc([], s1, parsed_sent) for parsed_sent in parsed]
    print(locs)
