import re

from sentence_transformers import SentenceTransformer

raw = """AI, search!
I can't log in.
help@example.com
CS4944 version 2.1

یہ ایک مثال ہے"""
lines = raw.split('\n')

for text in lines:
    parts = text.split()
    toks = re.findall(r'\b\w+\b', text, flags=re.UNICODE)
    print(repr(text), 'whitespace:', parts, len(parts))
    print('word-like:', toks, len(toks))

name = 'sentence-transformers/all-MiniLM-L6-v2'
model = SentenceTransformer(name, device='cpu')
for text in lines[:2]:
    print(text, model.tokenizer.tokenize(text))
