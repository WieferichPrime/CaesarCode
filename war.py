import re
from encode import encode
from collections import Counter


def war():
    f = open('warFirstPart.txt')
    text = f.read().lower()
    bigrammsGlobalOrder = Counter()
    for word in re.findall(r'[а-яё]+', text):
        for i in range(len(word) - 1):
            bigrammsGlobalOrder[word[i] + word[i + 1]] += 1
    bigrammsGlobalOrder = list(map(lambda item: item[0], bigrammsGlobalOrder.most_common()))

    pos = 0
    while pos < len(text):
        match = re.compile(r'[а-яё]+').match(text , pos)
        if match:
            text = text[:match.start()] + encode(word=match[0]) + text[match.end():]
            pos = match.end()
        else:
            pos += 1

    bigramms = Counter()
    open('war_encoded.txt', 'w').write(text)

    for word in re.findall(r'[а-яё]+', text):
        for i in range(len(word) - 1):
            bigramms[word[i] + word[i + 1]] += 1

    bigramms = list(map(lambda item: item[0], bigramms.most_common()))
    decoder = {}
    for i in range(len(bigramms)):
        if bigramms[i][0] not in decoder.keys() and bigramms[i][1] not in decoder.keys():
            decoder[bigramms[i][0]] = bigrammsGlobalOrder[i][0]
            decoder[bigramms[i][1]] = bigrammsGlobalOrder[i][1]

    pos = 0
    decoderKeys = decoder.keys()
    while pos < len(text):
        match = re.compile(r'[а-яё]').match(text, pos)
        if match and match[0] in decoderKeys:
            text = text[:match.start()] + decoder[match[0]] + text[match.end():]
            pos = match.end()
        else:
            pos += 1

    open('war_decoded.txt', 'w').write(text)