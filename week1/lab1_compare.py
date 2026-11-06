def symbolic(score, complete):
    if complete and score >= 70:
        return 'Review'
    return 'Hold'

def threshold(p):
    if p >= 0.70:
        return 'Review'
    return 'Hold'


cases = [
    ('complete_high', 82, True, 0.81),
    ('complete_low', 68, True, 0.74),
    ('incomplete_high', 91, False, 0.88),
    ('boundary', 70, True, 0.70),
]

print('case | score | complete | probability | symbolic | threshold | disagreement')
for name, score, complete, probability in cases:
    a = symbolic(score, complete)
    b = threshold(probability)
    diff = a != b
    print(name, score, complete, probability, a, b, diff, sep=' | ')
