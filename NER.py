from preprocessing import preproc

# Import your gazetteer


def isloc(raw, ind, sent, lemma, pos):

    # TASK: Write some rules that will find a city name.

        return False


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


def find_loc(raw, parsed):
    loc = []
    for sent in parsed:
        for ind in xrange(len(sent)):
            el = sent[ind]
            lemma = el[0]
            pos = el[1]
            if isloc(raw, ind, sent, lemma, pos):
                loc.append((ind, NER_recursion(ind, sent, lemma, pos)))
    return loc


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

    s1 = 'I am going to Lviv from New York'
    parsed = preproc(s1)
    locs = find_loc(s1, parsed)
    for loc in locs:
        print loc[1] + '\t' + loc_relation(loc, parsed[0])
