from lab6_search import Retriever

FAQ = [
    {'id': 'faq:password', 'question': 'How do I reset my password?',
     'answer': 'Use the recovery link on the login page.',
     'source': 'it_help.txt'},
    {'id': 'faq:submit', 'question': 'Where do I submit my assignment?',
     'answer': 'Use the assignment upload page in the learning portal.',
     'source': 'assessment.txt'},
    {'id': 'faq:late', 'question': 'Can illness justify a late submission?',
     'answer': 'Request an extension with medical evidence before the deadline.',
     'source': 'handbook.txt'},
    {'id': 'faq:portal', 'question': 'What file type must my assignment be?',
     'answer': 'Submit the final file as a PDF.',
     'source': 'assessment.txt'},
    {'id': 'faq:contractor', 'question': 'Can contractors work remotely?',
     'answer': 'Only when the signed contract permits remote work.',
     'source': 'hr_policy.txt'},
]


def build_bot(backend='tfidf'):
    records = []
    for r in FAQ:
        record = dict(r)
        record['text'] = r['question'] + ' ' + r['answer']
        records.append(record)
    return Retriever(records, backend)


def reply(engine, query):
    if not query.strip():
        return 'Please enter a question.'
    for r in FAQ:
        if query.strip().casefold() == r['question'].casefold():
            return r['answer'] + ' [source: ' + r['source'] + ']'
    hits = engine.search(query)
    if not hits:
        return 'No matching FAQ. Please contact the help desk.'
    lines = ['Possible matches; choose or rephrase your question:']
    for r, score in hits:
        lines.append(r['question'] + ' (similarity ' + format(score, '.3f') + ')')
    return '\n'.join(lines)


if __name__ == '__main__':
    bot = build_bot()
    print('FAQ assistant. Type exit to stop.')
    while True:
        query = input('You: ')
        if query.strip().lower() == 'exit':
            break
        print('Bot:', reply(bot, query))
