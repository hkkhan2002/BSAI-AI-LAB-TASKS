import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class Retriever:
    def __init__(self, records, backend='tfidf'):
        if not records:
            raise ValueError('Provide nonempty records')
        for r in records:
            if not r['text'].strip():
                raise ValueError('Provide nonempty records')
        self.records = records
        self.backend = backend
        texts = [r['text'] for r in records]
        if backend == 'tfidf':
            self.vectorizer = TfidfVectorizer()
            self.matrix = self.vectorizer.fit_transform(texts)
        elif backend == 'embedding':
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(
                'sentence-transformers/all-MiniLM-L6-v2', device='cpu')
            self.matrix = self.model.encode(texts, normalize_embeddings=True)
        else:
            raise ValueError('Use tfidf or embedding')

    def search(self, query, k=3, filters=None):
        if not query.strip() or k <= 0:
            return []
        if self.backend == 'tfidf':
            q = self.vectorizer.transform([query])
            if q.nnz == 0:
                return []
            scores = (q @ self.matrix.T).toarray()[0]
        else:
            q = self.model.encode([query], normalize_embeddings=True)[0]
            scores = self.matrix @ q
        keep = []
        for i, r in enumerate(self.records):
            ok = True
            for key, value in (filters or {}).items():
                if r.get(key) != value:
                    ok = False
            if ok:
                keep.append(i)
        order = sorted(keep, key=lambda i: (-float(scores[i]), i))
        return [(self.records[i], float(scores[i])) for i in order[:k]]


def show_hits(hits):
    if not hits:
        print('No matching records.')
    for record, score in hits:
        print(record['id'], 'score=' + format(score, '.3f'))
        print(record['text'])
