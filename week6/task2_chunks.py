import json
import re


def word_spans(text):
    return [(m.start(), m.end()) for m in re.finditer(r'\S+', text)]


def windows(text, size=40, overlap=10, offset=0):
    if size <= 0 or not 0 <= overlap < size:
        return []
    spans = word_spans(text)
    out = []
    for i in range(0, len(spans), size - overlap):
        j = min(i + size, len(spans))
        out.append((offset + spans[i][0], offset + spans[j - 1][1]))
        if j == len(spans):
            break
    return out


def sentence_chunks(text, size=40):
    if size <= 0:
        return []
    marks = [0]
    for m in re.finditer(r'[.!?]\s+', text):
        marks.append(m.end())
    marks.append(len(text))
    out = []
    piece = None
    n = 0
    for a, b in zip(marks, marks[1:]):
        segment = text[a:b]
        words = len(segment.split())
        if words == 0:
            continue
        if words > size:
            if piece is not None:
                out.append(piece)
            out.extend(windows(segment, size, 0, a))
            piece = None
            n = 0
        elif piece is not None and n + words <= size:
            piece = (piece[0], b)
            n = n + words
        else:
            if piece is not None:
                out.append(piece)
            piece = (a, b)
            n = words
    if piece is not None:
        out.append(piece)
    return out


def make_chunks(docs, strategy):
    all_chunks = []
    for doc_id, text in docs.items():
        if strategy == 'sentence':
            spans = sentence_chunks(text)
        else:
            spans = windows(text, 40, int(strategy))
        for i, (a, b) in enumerate(spans):
            all_chunks.append({'id': doc_id + ':' + str(i), 'doc': doc_id,
                               'start': a, 'end': b, 'text': text[a:b]})
    return all_chunks


if __name__ == '__main__':
    print('Empty text:', windows(''))
    print('Short text:', windows('short text'))
    bad = windows('a b', 2, 2)
    if bad == []:
        print('Invalid overlap rejected')
    else:
        print('ERROR: invalid overlap was accepted')
    long = ' '.join(['word'] * 95) + '.'
    print('Long sentence chunks:', len(sentence_chunks(long)), 'chunks, each under 40 words:',
          all(len(long[a:b].split()) <= 40 for a, b in sentence_chunks(long)))

    with open('corpus.json', encoding='utf-8') as f:
        docs = json.load(f)
    with open('queries.json', encoding='utf-8') as f:
        queries = json.load(f)

    for strategy in ['0', '10', 'sentence']:
        chunks = make_chunks(docs, strategy)
        total_words = 0
        for c in chunks:
            total_words = total_words + len(c['text'].split())
        original_words = 0
        for text in docs.values():
            original_words = original_words + len(text.split())
        print(strategy, 'chunks:', len(chunks),
              'total words:', total_words,
              'original words:', original_words,
              'repeated words:', total_words - original_words)

    for q in queries:
        if q['doc'] is None:
            continue
        for strategy in ['0', '10', 'sentence']:
            chunks = make_chunks(docs, strategy)
            found = False
            for c in chunks:
                if c['doc'] == q['doc'] and q['evidence'] in c['text']:
                    found = True
            print(q['query'][:40], strategy, 'evidence in one chunk:', found)
