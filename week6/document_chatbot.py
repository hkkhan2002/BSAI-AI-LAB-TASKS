import json

import sentence_transformers

from task2_chunks import make_chunks
from lab6_search import Retriever

with open('corpus.json', encoding='utf-8') as f:
    docs = json.load(f)
print('Using strategy:', '10', 'backend:', 'embedding')
engine = Retriever(make_chunks(docs, '10'), 'embedding')
print("Evidence assistant. Type exit to stop.")
while 1:
    query = input('Question: ')
    if query.strip().lower() == 'exit':
        break
    hits = engine.search(query)
    if not hits:
        print('No candidate evidence; rephrase or contact a human.')
        continue
    print('Candidate evidence; relevance must be checked:')
    for i in range(len(hits)):
        r, score = hits[i]
        number = i + 1
        rid = r['id']
        s = format(score, '.3f')
        a = r['start']
        b = r['end']
        print(number, rid, s, 'characters', a, b)
    chosen = input("Choose 1-3 to inspect; Enter if none apply: ")
    if chosen.isdigit() == False or int(chosen) < 1 or int(chosen) > len(hits):
        print('No answer selected. Rephrase or contact a human.')
        continue
    r, score = hits[int(chosen) - 1]
    print('Retrieved passage:', r['text'])
    print('Source:', r['doc'], 'characters', r['start'], r['end'])
